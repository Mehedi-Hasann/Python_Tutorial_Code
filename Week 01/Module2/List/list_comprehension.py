numbers = [45, 87, 65, 43, 85, 12, 26, 61]
odds=[]
for num in numbers:
    if num%2==1 and num%5==0:
        odds.append(num)
print(odds)

odd_numbers = [num for num in numbers]
print(odd_numbers)
odd_numbers = [num for num in numbers if num%2==1 if num%5==0]
print(odd_numbers)
odd_numbers = [num for num in numbers if num%2==1 and num%5==0]
print(odd_numbers)

players = ['shakib','mushfik','liton']
ages = [38,37,32]
age_combo=[]
for player in players:
    # print('player: ',player)
    for age in ages:
        # print('player: ',age)
        age_combo.append([player,age])
print(age_combo)

age_combo2 = [(player,age) for player in players for age in ages]
print(age_combo2)
age_combo2 = [[player,age] for player in players for age in ages]
print(age_combo2)