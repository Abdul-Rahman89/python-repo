# Indexing
str = "hello World" 
ch = str[0]
print(ch)
slicing = str[-3:-1]
print(slicing)
end = str.endswith("ld")
print(end)
str = str.capitalize()
print(str)

# Practice question
Fname = input("Enter your first name:")
length = len(Fname)
print(length)

# Condition
marks = 74

if(marks >= 90):
    grade = "A"
elif(marks >=80 and marks <= 90):
    grade = "B"
elif(marks >=70 and marks <= 80):
    grade = "C"
else:
    grade = "D"

print("Grade of the Sutdent is:", grade)                

# Palindrom
list1 = [1,2,3,2,1]
list2 = [1,2,3]

copy_list1 = list1.copy()
list1.reverse()
 
if(copy_list1 == list1):
    print("Palindorm")
else:
    print("No palindrom")
        