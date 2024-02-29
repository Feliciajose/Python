#3-C) Python Program to print Pyramid Pattern
rows = int(input("Enter number of rows: "))
for i in range(rows):
    for j in range(rows-i):
            print(end=" ")
    for j in range(i+1):
            print("*", end="")
    print()