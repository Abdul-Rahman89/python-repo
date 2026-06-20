# Same task ko bar bar krny se behtar h hum function bna ly ur usko call krty rhy. Block of code that perform specific task

def calc_sum(a,b):
    sum = a+b
    print(sum)
    return sum
calc_sum(12,4)

calc_sum(4,9)
# Mian purpose of function is reduced redundancy

def calc_avg(a,b,c):
    sum = a+b+c
    avg = sum/3
    print(avg)
    return avg
calc_avg(98,84,83)

# pactice questions
cities = ["mul", "lah", "toba","skp","fsd"]

def list_len(list):
    print(len(list))

# Print all item in one line
def print_list(list):
    for item in list:
        print(item, end=" ")    

list_len(cities)    
print_list(cities)


def calc_fact(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
        print(fact)
calc_fact(6)        


def convertor(usd):
    pkr = usd * 270
    print(usd,"USD =", pkr, "PKR =")
convertor(2)    
