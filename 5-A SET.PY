#5-A) To implement real-time/technical applications using Sets
# Set manipulation
CSE = {"PQT", "ADC", "SE", "DPSD", "DS", "OOP"}
IT = {"OS", "PQT", "DS", "SE", "OOP", "SS"}
print("CSE =",CSE)
print("IT =",IT)

# 1. Names of subjects in CSE
print("Subjects in CSE : ")
print(", ".join(CSE))

# 2. Names of subjects in IT
print("Subjects in IT : ")
print(", ".join(IT))

# 3. Names of subjects in CSE only
print("Names of subjects in CSE only : ", CSE.difference(IT))

# 4. Names of subjects in IT only
print("Names of subjects in IT only : ", IT.difference(CSE))

# 5. Names of subjects in both CSE and IT
CommonSubjects = CSE.intersection(IT)
print("Names of common subjects in CSE and IT :",CommonSubjects)

# 6. Names of subjects for either CSE or IT, but not in both
UniqueSubjects = CSE.symmetric_difference(IT)
print("Names of subjects for either CSE or IT, but not in both = ",
UniqueSubjects)

# 7. Names of all subjects.
Allsub=CSE.union(IT)
print("Names of all subjects : ", Allsub)