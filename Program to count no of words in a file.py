#Program to count no of words in a file
fs = open("First.txt","r")
fdata = fs.read()
L = fdata.split()
count=0
for i in L:
    count=count+1
print("Total no of words in the file:",count)
fs.close()