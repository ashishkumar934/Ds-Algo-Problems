import time 
import functools
def time_it(func):
  functools.wraps(func)
  def wrapper(*args,**kwargs):
    start_time=time.perf_counter()
    value = func(*args,**kwargs)
    end_time=time.perf_counter()
    print(f'Total Time Taken by {func.__name__!r} is {end_time-start_time}')
    return value
  return wrapper

@time_it
def calculate_n_natural_no_sum(number):
  output = (number*(number+1))/2
  return output

print(calculate_n_natural_no_sum(10))