#Program to copy from one file to another
fs=open("First.txt","r")
fd=open("Dest.txt","w")
fdata = fs.read()
fd.write(fdata)
print("File copied sucessfully!!!")
fs.close()
fd.close()