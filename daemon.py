#!/usr/bin/python3
# -*- coding: utf-8 -*-


"""
Ejemplo de creación de un "demonio" en sentido UNIX del término
"""


__author__ = "Sébastien CHAZALLET"
__copyright__ = "Copyright 2012"
__credits__ = ["Sébastien CHAZALLET", "InsPyration.org", "Ediciones ENI"]
__license__ = "GPL"
__version__ = "1.0"
__maintainer__ = "Sébastien CHAZALLET"
__email__ = "sebastien.chazallet@laposte.net"
__status__ = "Production"


import os
import time
import sys

pid=os.fork()
if pid==0:
    for i in range(60):
        print('Soy el hijo PID: %s y funciono. Mi padre es PID %s' % (os.getpid(), os.getppid()))
        time.sleep(1)
else:
    print('Soy el padre PID: %s, mi hijo es el PID %s' % (os.getpid(), pid))
    time.sleep(5)
    sys.exit(0)

