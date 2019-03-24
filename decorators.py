import time
import functools


def timing(f):
    @functools.wraps(f)
    def wrap(*args, **kwargs):
        time1 = time.time()
        ret = f(*args, **kwargs)
        time2 = time.time()
        print('{:s} function took {:.3f} ms'.format(f.__name__, (time2-time1)*1000.0))

        return ret
    return wrap


def easy_debugger(f):
    @functools.wraps(f)
    def wrap(*args, **kwargs):
        print('easy line to debug before {}'.format(f.__name__))
        ret = f(*args, **kwargs)
        print('easy line to debug after {}'.format(f.__name__))
        return ret
    return wrap


def run_multiple_times(times):
    def decorator(function):
        def wrapper(*args, **kwargs):
            result = None
            for i in range(times):
                result = function(*args, **kwargs)
            return result
        return wrapper
    return decorator
