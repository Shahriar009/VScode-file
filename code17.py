'''
class Car:
    def __init__(self,brand,mileage):
        self.mileage=mileage
        self.brand=brand
    def mileage_(self):
        print(f'The brand is {self.brand}')
        print(f'The mileage is {self.mileage}')
a=Car('BMW',33)
a.mileage_()
'''

from abc import ABC,abstractmethod

class Phone:


    abstractmethod
    
    def calling(self):
        '''
        print("5g call")
        '''
        pass

    def message(self):
        pass
    def music(self):
        pass
    def flahlight(self):
        pass
class Vivo(Phone):
    def camera(self):
        print('300px zoom')
    def calling(self):
        print("Special call")
class Sony(Phone):
    def camera(self):
        print('100px,zoom')
    def calling(self):
        print("Free call")
a=Vivo()
a.calling()
a.camera()
y=Sony()
y.calling()
y.camera()
