#5-B) To implement real-time/technical applications using Dictionaries
# Creating dictionary
D = {'AAAA':283, 'JJJJ':185, 'CCCC':307, 'GGGG':585, 'DDDD':427, 'EEEE':564,
'HHHH':370, 'BBBB':609}
print(D)
print("Component names - sorted alphabetically")
Comp_Names = sorted(D.keys())
print(Comp_Names)

print("Component values - sorted alphabetically")
print(sorted(D.values()))
print("Length of dictionary = ", len(D))

D.pop("HHHH")
print("Dictionary after deleting the component")
print(D)