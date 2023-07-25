def my_decorator(func_1):
  def wrapper():
    print('First Line')
    func_1('ashish')
    print('Third Line')
  return wrapper

@my_decorator
def func_1(name):
  print(f'Hello {name}')
  print('Second Line')

## Now func_1 is equivalent to my_decorator(func_1) which is returning the function

def my_decorator2(func_2):
  def wrapper(*args,**kwargs):
    print('added the wrapper functionality')
    func_2(*args,**kwargs)

  return wrapper

@my_decorator2
def func_2(first_name):
  print(f'HEllo {first_name}')

@my_decorator2
def func_3(int1,int2):
  print(int1+int2)
func_1()

func_2('ashish')
func_3(3,4)


## If we print help(func_1) it will say it is wrapper function. Which is technically correct but to point it 
## to original function we should add @functool.wraps.

import functools

def my_decorator3(func):
  @functools.wraps(func)
  def wrapper(*args,**kwargs):
    print('wrapper functionality')
    func(*args,**kwargs)
  return wrapper

@my_decorator3
def func_4():
  print('Hello')

#help(func_4)