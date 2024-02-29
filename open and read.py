# Open a file for writing
file = open("example.txt", "w")

# Write some data to the file
file.write("Hello, world!\n")
file.write("This is some sample data.\n")

# Close the file
file.close()

# Open the file for reading
file = open("example.txt", "r")

# Read the entire file into a string
data = file.read()
print(data)

# Close the file
file.close()

# Open the file for reading again
file = open("example.txt", "r")

# Read the file line by line and print each line
for line in file:
    print(line.strip())

# Close the file
file.close()

# Open the file for appending
file = open("example.txt", "a")

# Append some more data to the file
file.write("This is some more sample data.\n")

# Close the file
file.close()

# Open the file for reading again
file = open("example.txt", "r")

# Read the entire file into a list of lines
lines = file.readlines()
print(lines)

# Close the file
file.close()