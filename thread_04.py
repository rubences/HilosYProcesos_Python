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
import os


documents = [
	'http://docs.python.org/py3k/archives/python-3.2.2-docs-html.tar.bz2',
	'http://docs.python.org/archives/python-2.7.2-docs-html.tar.bz2',
	'http://docs.python.org/dev/archives/python-3.3a0-docs-html.tar.bz2',
]

t = time()

for document in documents:
	response = os.popen("wget %s" % document, "r")
	while True:
		line = response.readline()
		if not line:
			break

print('Descargas terminadas secuencialmente: %.2f' % (time() - t))

class Worker(Thread):
	def __init__(self, queue, document):
		self.queue = queue
		self.document = document
		Thread.__init__(self)
	def run(self):
		response = os.popen("wget %s" % self.document, "r")
		while True:
			line = response.readline()
			if not line:
				break
		self.queue.task_done()

try:
	t = time()
	q = Queue(3)
	for document in documents:
		print(1)
		task = Worker(q, document)
		print(2)
		task.start()
		print(3)
		q.put(task)
		print(4)
	print('Esperando el final de las descargas')
	q.join()
	print('Descargas terminadas: %.2f' % (time() - t))
except:
	print("Error: unable to start thread")


#Descargas terminadas secuencialmente: 13.89
#Descargas terminadas: 7.59

