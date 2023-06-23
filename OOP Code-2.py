

'''

alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}
aliens = [alien_0, alien_1, alien_2]
for alien in aliens:
 print(alien)



class Car:
    """A simple attempt to represent a car."""
def __init__(self, make, model, year):
    """Initialize attributes to describe a car."""
    self.make = make
    self.model = model
    self.year = year
def get_descriptive_name(self):
    """Return a neatly formatted descriptive name."""
    long_name = str(self.year) + ' ' + self.make + ' ' + self.model
    return long_name.title()
my_new_car = Car()
print(my_new_car.get_descriptive_name())
'''

#The __init__() Method for a Child Clas
class Bike():
    """That is a simple attempt to represent a caBike."""
    def __init__(self, make, model, year):
     self.make = make
     self.model = model
     self.year = year



class ElectricBike(Bike):
    """Represent aspects of a Bike, specific to electric bike."""
    def __init__(self, make, model, year):
     '''
     super().__init__(make, model, year)
     '''
my_tesla = ElectricBike('tesla', 'model s', 2016)
print(my_tesla)