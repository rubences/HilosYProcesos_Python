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

import os

def work(name):
	print('Inicio del trabajo: %s' % name)
	print('Pid: %s, parent: %s' % (os.getpid(), os.getppid()))
	print('Fin del trabajo: %s' % name)

print ('Flujo principal: %s' % os.getpid())
for i in range(2):
	p = Process(target=work, args=('Infos',))
	p.start()
	p.join()

