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


from threading import Thread, Lock
from queue import Queue

from time import time, ctime, sleep
from io import StringIO


def critical_fonction(buffer, letter, lock):
	with lock:
		for i in range(10):
			buffer.write(letter)
			sleep(0.1)
		buffer.write('\n')

class Worker(Thread):
	def __init__(self, queue, buffer, letter, lock):
		self.queue = queue
		self.buffer = buffer
		self.letter = letter
		self.lock = lock
		Thread.__init__(self)
	def run(self):
		for i in range(5):
			critical_fonction(self.buffer, self.letter, self.lock)
			sleep(0.1)
		self.queue.task_done()

try:
	lock = Lock()
	buffer = StringIO()
	q = Queue(3)
	t1 = Worker(q, buffer, "A", lock)
	t2 = Worker(q, buffer, "B", lock)
	t3 = Worker(q, buffer, "C", lock)
	t1.start()
	t2.start()
	t3.start()
	q.put(t1)
	q.put(t2)
	q.put(t3)
	q.join()
	print(buffer.getvalue())
except:
	print("Error: unable to start thread")

