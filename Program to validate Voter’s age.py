#Program to validate Voter’s age
try:
Name = input("Enter name : ")
Age = int(input("Enter Age : "))
if(Age<0):
    raise ValueError
elif (Age>=18):
    print(Name, " is eligible for voting.")
else:
    print(Name," is not Eligible for voting.")
except (ValueError):
    print("Value Error: invalid Age value.")