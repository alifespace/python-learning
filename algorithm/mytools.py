import time

def timeit(fn):
    def wrapper(*args, **kargs):
        t1 = time.time()
        result = fn(*args, **kargs)
        t2 = time.time()
        print("Function '%s' costs % seconds." % (fn.__name__, t2 - t1))
        return result
    
    return wrapper
