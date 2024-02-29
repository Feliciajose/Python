#LINEAR SEARCH 
a=[30,40,50,60,80]
print(a)
no=int(input("enter the value to search:"))
for i in range(0,len(a)):
    if(no==a[i]):
        print("found")
        break
else:
    print("not found")