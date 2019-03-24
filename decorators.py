import time


def timing(f):
    def wrap(*args):
        time1 = time.time()
        ret = f(*args)
        time2 = time.time()
        print('{:s} function took {:.3f} ms'.format(f.__name__, (time2-time1)*1000.0))

        return ret
    return wrap


def easy_debugger(f):
    def wrap(*args):
        print('easy line to debug before {}'.format(f.__name__))
        ret = f(*args)
        print('easy line to debug after {}'.format(f.__name__))
        return ret
    return wrap
