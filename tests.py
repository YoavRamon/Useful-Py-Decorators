import time

import decorators


@decorators.timing
def this_function_takes_time():
    time.sleep(3)


if __name__ == "__main__":
    this_function_takes_time()