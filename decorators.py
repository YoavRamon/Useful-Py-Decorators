import sys
import time
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
