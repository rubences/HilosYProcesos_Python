#!/usr/bin/python3
# -*- coding: utf-8 -*-


"""
Ilustración del funcionamiento del módulo multiprocessing
"""


__author__ = "Sébastien CHAZALLET"
__copyright__ = "Copyright 2012"
__credits__ = ["Sébastien CHAZALLET", "InsPyration.org", "Ediciones ENI"]
__license__ = "GPL"
__version__ = "1.0"
__maintainer__ = "Sébastien CHAZALLET"
__email__ = "sebastien.chazallet@laposte.net"
__status__ = "Production"


from multiprocessing import Process, Pipe


def reader(o):
	while True:
		data = o.recv()
		print(data)
		if data == '#':
			return

def writer(i):
	for data in ['Message', 42, '#']:
		i.send(data)

i, o = Pipe()
pr = Process(target=reader, args=(o,))
pr.start()
pw = Process(target=writer, args=(i,))
pw.start()

pw.join()
pr.join()

