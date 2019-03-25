import time

from decorators import timing, print_with_color, easy_debugger, run_multiple_times, handle_exception


@timing
def this_function_takes_time():
    time.sleep(3)


@print_with_color('blue')
@easy_debugger
def this_function_does_something():
    print('something')


@run_multiple_times(3)
def this_print_words(words):
    print(words)


@handle_exception
def buggy_function():
    raise FileExistsError('This file dosen\'t exist!')


if __name__ == "__main__":

    this_function_takes_time()
    buggy_function()
    this_function_does_something()
    this_print_words('Yoav Love Halav')
