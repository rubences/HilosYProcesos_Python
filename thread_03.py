#!/usr/bin/python3
# -*- coding: utf-8 -*-


"""
Ilustración del funcionamiento a bajo nivel de los threads
"""


__author__ = "Sébastien CHAZALLET"
__copyright__ = "Copyright 2012"
__credits__ = ["Sébastien CHAZALLET", "InsPyration.org", "Ediciones ENI"]
__license__ = "GPL"
__version__ = "1.0"
__maintainer__ = "Sébastien CHAZALLET"
__email__ = "sebastien.chazallet@laposte.net"
__status__ = "Production"


from threading import Thread
from queue import Queue

from time import time, ctime, sleep


class Worker(Thread):
	def __init__(self, queue, name, delay):
		print('Creación del worker %s' % name)
		self.queue = queue
		self.delay = delay
		self.job_ended = False
		Thread.__init__(self, name=name)
	def run(self):
		for i in range(5):
			if self.job_ended:
				print('Parada forzada de: %s' % self.getName())
				self.queue.task_done()
				return
			print("%s: Llamada %s, %s" % (self.getName(), i, ctime(time())))
			sleep(self.delay)
		print('Parada natural de: %s' % self.getName())
		self.queue.task_done()

class Stopper(Thread):
	def __init__(self, threads, delay):
		print('Creación del stopper')
		self.delay = delay
		self.threads = threads
		Thread.__init__(self)
	def run(self):
		sleep(self.delay)
		print('Solicitud de parada de las tareas')
		for t in self.threads:
			t.job_ended = True

try:
	q = Queue(3)
	t1 = Worker(q, "T1", 1)
	t2 = Worker(q, "T2", 2)
	t3 = Worker(q, "T3", 3)
	t1.start()
	t2.start()
	t3.start()
	q.put(t1)
	q.put(t2)
	q.put(t3)
	s = Stopper((t1, t2, t3), 6)
	s.start()
	print('Esperando el final de las tareas')
	q.join()
	print('Tareas terminadas, se retoma el flujo principal de las instrucciones')
except:
	print("Error: unable to start thread")

