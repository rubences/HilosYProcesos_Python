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


from threading import Thread, BoundedSemaphore

from time import sleep


class Worker(Thread):
	def __init__(self, semaphore, name, delay):
		print('Creación del worker %s' % name)
		self.semaphore = semaphore
		self.delay = delay
		Thread.__init__(self, name=name)
	def run(self):
		with self.semaphore:
			print("Thread > %s" % self.getName())
			sleep(self.delay *0.001)
			print("Thread < %s" % self.getName())

try:
	s = BoundedSemaphore(value=3)
	for i in range(10):
		t = Worker(s, 'T%s' % i, i)
		t.start()
except:
	print("Error: unable to start thread")




"""
pool_sema.acquire()
conn = connectdb()
... use connection ...
conn.close()
pool_sema.release()
"""



