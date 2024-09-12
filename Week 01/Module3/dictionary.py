#key value pair/dictionary/object/hash table/overlap with set
person = {
    'name':'kala pakhi',
    'address':'kalipur',
    'age':23,
    'job':'facebooker'
}
print(person)
print(person['age'])
print(person['job'])

print(person.keys())
print(person.values())
#mutable
person['language'] = 'python'
print(person)
person['name'] = 'sada pakhi'
print(person)

# dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])

#looping

for item in person: #shudu key gulo paua jai
    print(item)
#special looping
for item in person.items():
    print(item)
for key,value in person.items():
    print(key,value)