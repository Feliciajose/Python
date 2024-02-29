def h(n):
    s = 0
    for i in range(1,n+1):
        if n%i > 0:
           s = s+1
           print(s)
    return(s)
    
h1=h(53)-h(52)
print(h1)