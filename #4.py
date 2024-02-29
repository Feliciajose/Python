#4.B) Materials required for construction of a building using tuples
BuildingMaterials = ('Cement', 'Bricks', 'Blocks', 'Wooden Products', 'Hardware and
Fixtures', 'Natural Stones','Doors', 'Windows', 'Modular Kitchen', Sand', 'Aggregates',
'Tiles')
ElectricalMaterials = ('Conduit Pipes and Fittings', 'Wires and Cables', 'Modular
switches and sockets', 'Electric Panels', 'Switch Gear')
print("Created tuple : ")
print("Building Materials : ",BuildingMaterials)
print("Electrical Materials : ",ElectricalMaterials)

# Accessing elements by index
print("First element in tuple : ",BuildingMaterials[0])
print("Last element in tuple : ",BuildingMaterials[-1])

# Splicing
print("First 5 elements in tuple : ",BuildingMaterials[0:5])

# length of tuple
print("Length of tuple : ",len(BuildingMaterials))

# Concatenation, repetition
print("Concatenation operation")
AllMaterials = BuildingMaterials+ElectricalMaterials
print("All materials")
print(AllMaterials)
print("Repetition operation")
print(AllMaterials*2)

# Membership operator
SearchMaterial = input("Enter material to search : ")
if SearchMaterial in AllMaterials:
print("Material present in tuple.")

else:
print("Material not present in tuple.")

# Iteration operation
print("Iteration operation")
print("Materials required for construction of a building: ")
for mat in AllMaterials:
print(mat)