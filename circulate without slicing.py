a=list(input("enter the list"))
print(a)
for i in range(1,len(a),1):
    b= a.pop(0)
    a.append(b)
    print(a)