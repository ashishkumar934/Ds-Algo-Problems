class Person:
  def __init__(self,*args,**kwargs):
    for i,v in kwargs.items():
      self.i = v
  
  def __str__(self):
    print('Hello I am a string')
    return f'Hello I am {self.name}'

  def __repr__(self):
    return self

user1=Person(name='ashish',age=25,country='India')
print(dir(user1))
# dir(Person)
# str(user1)
