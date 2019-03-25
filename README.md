# Useful-Py-Decorators
Useful decorators in python3 that I use a lot

### Basic Decorators

**timing** - checks the time that it took the function to run and print it in milliseconds.

```python
from decorators import timing
import time

@timing
def this_function_takes_time():
    time.sleep(3)
```
Should output: `this_function_takes_time function took 3002.590 ms`

**easy_debugger** - Adds an easy kine to put a debugger breakdown whenever the function starts or stops.
```python
from decorators import easy_debugger

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
from decorators import print_with_color

@print_with_color('red')
def this_function_does_something():
    print('something')
``` 
Should output `something` in red.

**run_multiple_times** - Makes the function run multiple times.
```python
from decorators import run_multiple_times

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