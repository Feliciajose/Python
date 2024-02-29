def power(base,exp):
    if(exp==1):
        return(base)
    else:
        return(base*power(base,exp-1))
base=int(input("enter base:"))
exp=int(input("enter exponential value"))
result=power(base,exp)
print("result",result)