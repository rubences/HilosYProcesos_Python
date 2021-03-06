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


from multiprocessing import Process

from time import sleep


def work(name):
	print('Inicio del trabajo: %s' % name)
	for j in range(2):
		for i in range(10):
			sleep(0.01)
			print('.', sep='', end='')
		print('.')
	print('Fin del trabajo: %s' % name)

p = Process(target=work, args=('Test',))
p.start()
print('Esperando el final del proceso')
for j in range(4):
	for i in range(10):
		sleep(0.01)
		print('o', sep='', end='')
	print('o')

print('Fin de la espera')
p.join()

