#!/usr/bin/python3.4

from itertools import permutations
import asyncio

@asyncio.coroutine
def nqueens_async_coroutine(future, n):
    columns=range(n)
    for board in permutations(columns):
        if n == len(set(board[i]+i for i in columns)) \
             == len(set(board[i]-i for i in columns)):
            future.set_result(board)
def nqueens_async(n):
    loop = asyncio.get_event_loop()
    future = asyncio.Future()
    asyncio.Task(nqueens_async_coroutine(future, n))
    loop.run_until_complete(future)
    print(future.result())
    loop.close()

if __name__ == '__main__'
    t0=time()
    res=nqueens_workers(4)
    t1=time()
    print('4-Damas en asincronía  : %12.9f segundos' % (t1-t0))

