#insertion sort 
a=[5,2,4,1,3]
print("un sorted array:",a)
n=len(a)
for i in range (1,n):
    key=a[i]
    j=i-1
    while(j>=0) and (key<a[j]):
        a[j+1]=a[j]
        j=j-1
        a[j+1]=key
print("sorted array:",a)