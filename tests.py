import time

import decorators


@decorators.timing
def this_function_takes_time():
    time.sleep(3)


@decorators.print_with_color('blue')
@decorators.easy_debugger
def this_function_does_something():
    time.sleep(1)


@decorators.run_multiple_times(3)
def this_print_words(words):
    print(words)


if __name__ == "__main__":

    this_function_takes_time()
    this_function_does_something()
    this_print_words('Yoav Love Halav')
