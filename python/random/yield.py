def countDown(n):
    while n >0:
        yield n
        n-=1

def writer():
    """a coroutine that pretends to write data sent to it"""
    while True:
        w = (yield)
        print('>> ',w)