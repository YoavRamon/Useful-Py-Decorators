# Useful-Py-Decorators
Useful decorators in python3 that I use a lot

## Installation
To install this package run:
```bash
pip install https://github.com/YoavRamon/Useful-Py-Decorators/releases/download/v1.0/useful-py-decorators-1.0.zip
``` 

## Usage
### Basic Decorators

**timing** - checks the time that it took the function to run and print it in milliseconds.

```python
from decorators.basic import timing
import time

@timing
def this_function_takes_time():
    time.sleep(3)
```
Should output: `this_function_takes_time function took 3002.590 ms`

**easy_debugger** - Adds an easy kine to put a debugger breakdown whenever the function starts or stops.
```python
from decorators.basic import easy_debugger

@easy_debugger
def this_function_does_something():
    print('something')
``` 
Should output: 
```
easy line to debug before this_function_does_something
something
easy line to debug after this_function_does_something
```

**print_with_color** - Makes the function to print it outputs with certain color. 
Possible colors are: *black, red, green, yellow, blue, magenta, cyan and white*
```python
from decorators.basic import print_with_color

@print_with_color('red')
def this_function_does_something():
    print('something')
``` 
Should output `something` in red.

**run_multiple_times** - Makes the function run multiple times.
```python
from decorators.basic import run_multiple_times

@run_multiple_times(3)
def print_string(text):
    print(text)
```
Should output (With `text='Yoav Love Halav'`):
```
Yoav Love Halav
Yoav Love Halav
Yoav Love Halav
```

**handle_exception** - Catches any exception, prints it and let the code run after the function.
```python
from decorators.basic import handle_exception

@handle_exception
def buggy_function():
    raise FileExistsError('This file dosen\'t exist!')

buggy_function()
print('some code after')
```
Should output:
```
* * * * * That exception was ignored * * * * *
* Traceback (most recent call last):
*   File "/Useful-Py-Decorators/decorators.py", line 94, in wrap
*     ret = f(*args, **kwargs)
*   File "/Useful-Py-Decorators/tests.py", line 4, in buggy_function
*     raise FileExistsError('This file dosen\'t exist!')
* FileExistsError: This file dosen't exist!
* 
* * * * * * * * * * * * * * * * * * * * * * * *
some code after
```

**fix_random** - Makes random functions reproducible and consistent.
```python
import random
from decorators.basic import run_multiple_times, fix_random

@run_multiple_times(3)
@fix_random()
def print_random_number():
    print(random.random())
```
Should output:
```
0.5155408159323152
0.5155408159323152
0.5155408159323152
```

## Build package
The distribution is being built with setuptools. To build from source run the following commands:
```bash
git clone https://github.com/YoavRamon/Useful-Py-Decorators
python setup.py sdist --formats=zip
```
This will create the distribution at `dist/useful-py-decorators-<Version>.zip`
