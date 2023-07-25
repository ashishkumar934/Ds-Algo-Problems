"""
Calling the methods inside the class
"""
class Name:
  def __init__(self):
    self.name = 'ashish'
    self.__pv='singh'
    self._pv2='kumar'
    
  def rename(self,new_name):
    self.name=new_name

  def get_name(self):
    return self.name

print('Classes 2')

person1= Name()
print(person1.name)
person1.rename('Ashish Kumar Singh')
print(person1.get_name())

### Example of the Name Mangling in Python Classes
print(person1._Name__pv)
person1._Name__pv='kumar singh'
print(person1._Name__pv)

print(person1._pv2) 
#print(person1.__pv) This expression throws the error