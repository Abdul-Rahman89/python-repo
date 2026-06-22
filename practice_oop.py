# Practice question
class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
    def get_avg(self):
        sum = 0
        for val in self.marks:
            sum += val
        print("hi", self.name, "your avg score is :", sum/3)    
 
s3 = Student("Abdullah :", [89,90,91])
s3.get_avg()    

# 2nd practice question

class Account:
    def __init__(self,bal,acc):
        self.balance = bal
        self.accont_no = acc

    def debit(self,amount):
        self.balance -= amount
        print("Rs :", amount,"was debeted")
        print("Total Balance", self.get_balance())
    def credit(self,amount):
        self.balance += amount
        print("Rs :", amount,"was credited")
        print("Total Balance",self.get_balance())
    def get_balance(self):
        return self.balance         

acc1 = Account(10000,12345)
acc1.debit(199)
acc1.credit(299)
        