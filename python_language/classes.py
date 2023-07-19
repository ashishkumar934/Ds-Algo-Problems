class max_and_min:
  
  lastName='kumar'
  def __init__(self):
    print(self)
    self.name='max and min'
    self.gender='male'
    self.count=0
    self.lastName='singh'

  def change_name(self,name_to_change):
    print(self)
    self.name=name_to_change

  @staticmethod
  def print_name():
    print('Name is Called')
    print('LastName',max_and_min.lastName)
    max_and_min.lastName='kumar2'


pair1=max_and_min()
print(pair1)
pair1.change_name('krishna')
print(pair1.name)
print(pair1.lastName)

max_and_min.print_name()
print(max_and_min.lastName)
