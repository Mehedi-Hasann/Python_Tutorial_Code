#We saw that lists and strings have many common properties, such as indexing and slicing operations
def multiple():
    return 3,4
print(multiple())

things = 'pen','tripod','water bottle','charger','phone','web cam'
print(things)
print(things[0])
print(things[-2])
print(things[3:6])
if 'phone' in things:
    print('exist')
for item in things:
    print(item)
# things[0]='wagon' possible na krn immutable
print(len(things))

mega = ([2,3,4],[6,7,8])
print(type(mega))
print(mega[0])
mega[0][1]=666 #tuple change kora jaina,kintu er vitor mutable jinis thakle sekhane gyea change kora jai
print(mega)
