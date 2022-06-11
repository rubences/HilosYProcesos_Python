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
from time import time, ctime, sleep


class Worker(Thread):
	def __init__(self, name, delay):
		print('Creación del worker %s' % name)
		self.delay = delay
		self.job_ended = False
		Thread.__init__(self, name=name)
	def run(self):
		for i in range(10):
			if self.job_ended:
				print('Parada forzada de: %s' % self.getName())
				return
			print("%s: Llamada %s, %s" % (self.getName(), i, ctime(time())))
			sleep(self.delay)
		print('Parada natural de: %s' % self.getName())

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
	t1 = Worker("T1", 1)
	t2 = Worker("T2", 2)
	t3 = Worker("T3", 3)
	s = Stopper((t1, t2, t3), 15)
	t1.start()
	t2.start()
	t3.start()
	s.start()
except:
	print("Error: unable to start thread")

