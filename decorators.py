import sys
import time
import random
import traceback
import builtins
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
    def decorator(f):
        @functools.wraps(f)
        def wrap(*args, **kwargs):
            result = None
            for i in range(times):
                result = f(*args, **kwargs)
            return result
        return wrap
    return decorator


def print_with_color(color):
    colors = {'black': '30', 'red': '31', 'green': '32', 'yellow': '33',
              'blue': '34', 'magenta': '35', 'cyan': '36', 'white': '37'}
    base_data = '\033[{}m'.format(colors.get(color) or '0')

    def _print(*args, **kwargs):
        """The new-style print function from py3k."""
        fp = kwargs.pop("file", sys.stdout)
        if fp is None:
            return

        def write(data):
            if not isinstance(data, str):
                data = str(data)
            fp.write(data)

        sep = kwargs.pop("sep", None)
        end = kwargs.pop("end", None)

        if kwargs:
            raise TypeError("invalid keyword arguments to print()")

        newline = "\n"
        space = " "
        if sep is None:
            sep = space
        if end is None:
            end = newline
        write(base_data)  # Prints the color ANSI code
        for i, arg in enumerate(args):
            if i:
                write(sep)
            write(arg)
        write(end)
        write('\033[0m')  # Resets the color ANSI code

    def decorator(f):
        @functools.wraps(f)
        def wrap(*args, **kwargs):
            old_print = builtins.print
            builtins.print = _print
            result = f(*args, **kwargs)
            builtins.print = old_print
            return result
        return wrap
    return decorator


def handle_exception(f):
    @functools.wraps(f)
    def wrap(*args, **kwargs):
        try:
            ret = f(*args, **kwargs)
            return ret
        except Exception as ex:
            tb = traceback.format_exc()
            print('\033[32m* * * * * That exception was ignored * * * * *\033[31m')
            for line in tb.split('\n'):
                print('\033[32m* \033[31m{}'.format(line))
            print('\033[32m* * * * * * * * * * * * * * * * * * * * * * * *\033[0m')
    return wrap


def fix_random(seed=1014):
    def decorator(f):
        @functools.wraps(f)
        def wrap(*args, **kwargs):
            random.seed(seed)
            return f(*args, **kwargs)
        return wrap
    return decorator
