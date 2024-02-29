#4-A Items present in a library using list
list1 = [ 'Books', 'Documents', 'Newspaper', 'Ebook', 'Periodicals' ]
print(list1) # Prints complete list
print(list1[0]) # Prints first element of the list
print(list1[1:3]) # Prints elements starting from 2nd till 3rd
print(list1[2:]) # Prints elements starting from 3rd element
print(list1[-1]) # Prints last element
print(list1[-3:]) # Prints last 3 elements
print(list1[-4:-1]) # Prints last 4 elements -1
list1.append('Audio books')
print(list1) # Prints list after appending
list1.sort()
print(list1) # Prints list after sorting
list1.remove('Ebook')
print(list1) # list after removing the above element
list1.insert(3,'CDs')
print(list1)