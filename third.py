# Dictionary means key value pair like object in JS, Unorder, mutalbe, don't allow duplicate
info = {
    "Name" : "Mani",
    "Age" : 24,
    "Marks" : [48,50,52] 
}
print(info)

student = {
    "Name" : "Mani",
     "subject" : {
         "phy" : 97,
         "che" : 84,
         "math" : 98
     }
}
print(student["subject"])

# Sets is the collection of unorder items, and must be unique and immutable means sets are itself mutlable but the value are inmutable