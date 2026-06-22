class Studnet:
    # Constructor in Python , Self parameter is the reference of the current object of class
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
    def welcome(self):
        print("Welcome sutduend",self.name)
    def get_makrs(self):
        return self.marks    

s1 = Studnet("Mani",98)
s1.welcome()
print(s1.get_makrs())  
s2 = Studnet("Ahmad",84)
s2.welcome()
print(s2.get_makrs())

# Class have 2 properties one is the attribute and 2nd one is method --> means fuction that perform for complete the work. 


  