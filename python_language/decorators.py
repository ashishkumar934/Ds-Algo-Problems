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


#### Fancy Decorators ###
#1. Nested 
#2. With Arguments
#3. Over class
#4. Class as Decorator
#5. Stateful Decorator

## StateFul Decorator ##

def stateful_decorator(func):
  
  def wrapper(*args,**kwargs):
    print('Wrapper INitiated')
    func(*args,**kwargs)
    wrapper.a+=1
    print(wrapper.a)
  wrapper.a=0 ## This is the function attribute different from the variable. As Function is also the object so it also has the attributes 
  return wrapper

@stateful_decorator
def say_hi():
  print('Hi')

say_hi()
say_hi()
say_hi()


## Stateful Decoraters are mostly used with the class as decorators

class Decorator_Class:
  def __init__(self):
    self.count=0

  ## This function is executed whenver the class object is called
  def __call__(self):
    self.count+=1
    print(f"Current count is {self.count}")

obj1=Decorator_Class()
obj1()
obj1()


class CountCalls:
  def __init__ (self,func):
    functools.update_wrapper(self, func)
    self.func=func
    self.num_calls=0
  
  def __call__(self,*args,**kwargs):
    self.num_calls+=1
    print(f'Current Call is {self.num_calls}')
    return self.func(*args,*kwargs)

@CountCalls
def greetings():
  print('Hello Sir! How are you?')

greetings()
greetings()


## Caching or Memoization -

def cache(func):
    """Keep a cache of previous function calls"""
    @functools.wraps(func)
    def wrapper_cache(*args, **kwargs):
        print(args)
        print(kwargs.items())
        cache_key = args + tuple(kwargs.items())
        print(cache_key)
        if cache_key not in wrapper_cache.cache:
            wrapper_cache.cache[cache_key] = func(*args, **kwargs)
        return wrapper_cache.cache[cache_key]
    wrapper_cache.cache = dict()
    return wrapper_cache

@cache
def fibonacci(num,kt='10'):
    if num < 2:
        return num
    return fibonacci(num - 1,kt='10') + fibonacci(num - 2,kt='10')

print(fibonacci(10,kt='10'))
#print(fibonacci.cache)
## Real World Examples 


## Validating JSON 

@app.route("/grade", methods=["POST"])
def update_grade():
    json_data = request.get_json()
    if "student_id" not in json_data:
        abort(400)
    # Update database
    return "success!"


from flask import Flask, request, abort
import functools
app = Flask(__name__)

def validate_json(*expected_args):                  # 1
    def decorator_validate_json(func):
        @functools.wraps(func)
        def wrapper_validate_json(*args, **kwargs):
            json_object = request.get_json()
            for expected_arg in expected_args:      # 2
                if expected_arg not in json_object:
                    abort(400)
            return func(*args, **kwargs)
        return wrapper_validate_json
    return decorator_validate_json


@app.route("/grade", methods=["POST"])
@validate_json("student_id")
def update_grade():
    json_data = request.get_json()
    # Update database.
    return "success!"

