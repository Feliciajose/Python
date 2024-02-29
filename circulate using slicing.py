# using slicing technique
a=list(input("enter the list"))
print(a)
for i in range(1,len(a),1):
    f=(a[i:]+a[:i])
    print(f)