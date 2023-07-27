#  * -> is the unpacking operator which matters not the args name
def add_numbers_2(*ints):
  sum=0
  for i in ints:
    sum+=i
  print(sum)
def add_numbers(*args):
  print(args)
  for i in args:
    print(i)

# **-> Is the unpacking operator it returns the name and value pair. Used for keywords arguments

def print_name(**kwargs):
  print(kwargs)
  for i in kwargs.values():
    print(i)

### Order in which we should call the arguments
 # 1. Standard arguments
 # 2. *args
 # 3. **kwargs

# If positional argument is given after kwargs then invalid syntax
def check_order(name,*args,**kwargs):
  print(name)
  print(args)
  print(kwargs)
add_numbers(1,2,3)
add_numbers_2(1,2,3)
print_name(first='ashish',second='kumar')
check_order('ashish',2,3,'krishna',hello='hi',)
check_order(3,jio='jio')
#check_order(3,jio='jio','krishna') ## Error Line positional argument follows keyword argument


##  * and ** can also be used as the unpacking operator. Following example.
*b, =[1,2,3]
print(b)
print(*b)
c=[1,2,3]
print(*c)

list_1=[1,2,3]
list_2=[4,5,6]
print([*list_1,*list_2])
dict_1={'first_name':'ashish'}
dict_2={'second_name':'kumar'}
print({**dict_1,**dict_2})