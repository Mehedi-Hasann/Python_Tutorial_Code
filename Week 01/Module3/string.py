name1 = 'sakib\'s khan' #escape
name2 = "sakib khan"
name3 = """sakib khan"""
print(name1)
print(name2)
print(name3)

for char in name2:
    print(char)
print(name2[3])
print(name2[1:6])
print(name2[-1])
print(name2[::-1])
#mutable means changeable
#inmutable means unchangeabe
# name2[0] = 'R' kora jaina krn immutable
print(name2)
if 'khan' in name2:
    print('exist')
print(name2.upper())