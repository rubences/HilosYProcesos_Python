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


from multiprocessing import Process, Value

from time import sleep


def add(value):
	for i in range(3):
		value.acquire()
		value.value += 2
		value.release()
		print(value.value)
		sleep(1)

def sub(value):
	while value.value > 0:
		value.acquire()
		value.value -= 1
		value.release()
		print(value.value)
		sleep(2)

value = Value('i', 0)
pa = Process(target=add, args=(value,))
pa.start()
sleep(0.5)
ps = Process(target=sub, args=(value,))
ps.start()

pa.join()
ps.join()

from multiprocessing import Array
arr = Array('d', [1.0, 1.4, 1.7, 1.9, 2.0])
