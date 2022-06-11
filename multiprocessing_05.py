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


from multiprocessing import Pool

import os

def f(x):
	return x, os.getpid()

pool = Pool(processes=4)

print(pool.map(f, range(10)))

result = pool.apply_async(f, [10])
print(result.get(timeout=1))

result = pool.apply(f, [16])
print(result.get(timeout=1))

result_id = pool.map_async(f, range(10))
result_id.get(timeout=0.0000001)


it = pool.imap(f, range(3))
print(next(it))

def g(x):
	print('send %s' % x)
	return f(x)

for x, pid in pool.imap(g, range(3)):
	print('recv %s (%s)' % (x, pid))


from multiprocessing import Pipe


i, o = Pipe()
i.send(42)
o.recv()
i.send('Hello')
o.recv()












