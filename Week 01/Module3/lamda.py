# def double(x):
#     return x*2

# result = double(44)
# print(result)
doubled = lambda num : num*2
squared = lambda num : num*num
result = doubled(44)
output = squared(9)
print(result,output)

add = lambda x,y : x + y
sum = add(11,33)
print(sum)


numbers = [12,56,98,78,56,12,6,12]
# doubled_nums = map(doubled,numbers)
doubled_nums = map(lambda x:x*2,numbers) #sobar upr chalabe
print(numbers)
print(list(doubled_nums))


actors = [
    {'name':'sabana', 'age': 65},
    {'name':'sabnoor', 'age': 45},
    {'name':'sabila nur', 'age': 30},
    {'name':'srabonti', 'age': 38},
    {'name':'shaon', 'age': 47}
]
juniors = filter(lambda actor : actor['age']<40,actors) #kono akta sorto thakbe,sortor upr base kore
fivers = filter(lambda actor: actor['age']%5==0,actors) 
print(list(juniors))
print(list(fivers))