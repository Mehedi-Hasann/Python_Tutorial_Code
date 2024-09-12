def sum(num1,num2):
    result = num1+num2
    return result
total = sum(99,11)
# print('total: ',total)

#args (touple er moto kaj kore)
def all_sum(num1,num2,*numbers):
    print(numbers)
    sum = 0
    for num in numbers:
        print(num)
        sum = sum + num
    return sum
total = all_sum(10,20,30,40,50,60)
print('all sum: ',total)

#return multiple things from an array

def a_lot(num1,num2):
    sum = num1 + num2
    mult = num1*num2
    remain = num1-num2
    #return [sum,mult,remain]
    return sum,mult,remain
print(a_lot(10,20))
#you can access global variable without using the global keyword
#if u want to modify a global variable, u have to use the global keyword