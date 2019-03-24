import time

import decorators


@decorators.timing
def this_function_takes_time():
    time.sleep(3)


@decorators.easy_debuger
def this_function_does_something():
    time.sleep(1)


if __name__ == "__main__":
    this_function_takes_time()
    this_function_does_something()