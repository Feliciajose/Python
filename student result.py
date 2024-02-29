name=input("enter the name ")
rollno=int(input("enter the roll no"))
eng=int(input("enter the mark in eng"))
maths=int(input("enter the mark in maths"))
phy=int(input("enter the mark in phy"))
chem=int(input("enter the mark in chem"))
pspp=int(input("enter the mark in pspp"))
total=(eng + maths + phy + chem + pspp)
avg=total/5
if("avg>=50"):
    print("result is pass")
if(avg>=90):
    print("grade is A")
elif("avg>=80"):
    print("grade is B")
elif("avg>=70"):
    print("grade is C")
elif("avg>=60"):
    print("grade is D")
elif("avg>=50"):
    print("grade is F")             
else:
    print("result is fail")   