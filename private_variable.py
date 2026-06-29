"""With the help of __ dounle underscore we can make a variable private in python and also with the help of super key word we can 
access the constructor of parent class in child class and @static method means this can be create one time and every object of this class
can be used when they want and if we want to change the class attribute so we can not do this with the help of static method so for
this we can use class method"""

class Car:
    def __init__(self,type):
        self.type = type

    @staticmethod
    def start():
        print("Car is started..")

    @staticmethod
    def stop():
        print("Car is stopped..")        
class ToyotaCar(Car):
    def __init__(self,name, type):
        super().__init__(type)
        self.name = name
        super().start()        

car1 = ToyotaCar("Pirus", "Electric") 
print(car1.type)       