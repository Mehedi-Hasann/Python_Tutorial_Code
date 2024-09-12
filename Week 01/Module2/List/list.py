#list , array is same(simple terms)
#index      0   1  2   3   4   5   6   7   8
numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90]
#index     -9  -8  -7  -6  -5  -4  -3  -2  -1

print(numbers[3],numbers[-3])
#output: 40 70

#list(start : end)
print(numbers[2:6])
#output: [30, 40, 50, 60]

#list(start : end : step)
print(numbers[1:7:1])
#output: [20, 30, 40, 50, 60, 70]
print(numbers[1:7:2])
#output: [20, 40, 60]
print(numbers[2:7:-1])
#output: []
print(numbers[7:2:-1])
#output: [80, 70, 60, 50, 40]
print(numbers[4:])
#output: [50, 60, 70, 80, 90]
print(numbers[:5])
#output: [10, 20, 30, 40, 50]
print(numbers[:])    #shortcut to copy a list
#output: [10, 20, 30, 40, 50, 60, 70, 80, 90]
print(numbers[::-1]) # shortcut to reverse a list
#output: [90, 80, 70, 60, 50, 40, 30, 20, 10]

fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
fruits.count('apple') 
#output: 2
fruits.count('tangerine')
#output: 0
fruits.index('banana')
#output: 3
fruits.index('banana', 4)  # Find next banana starting at position 4
#output: 6
fruits.reverse()
fruits
#output: ['banana', 'apple', 'kiwi', 'banana', 'pear', 'apple', 'orange']
fruits.append('grape')  #Add an item to the end of the list
fruits
#output: ['banana', 'apple', 'kiwi', 'banana', 'pear', 'apple', 'orange', 'grape']
fruits.sort()
fruits
#output: ['apple', 'apple', 'banana', 'banana', 'grape', 'kiwi', 'orange', 'pear']
fruits.pop()    #removes and returns the last item in the list
#output: 'pear'
# fruits.pop() #remove the item at the given position in the list, and return it
# print(fruits)

numbers = [12,45,98,68,98]
if 98 in numbers:
    numbers.remove(98)  #Remove the first item from the list whose value is equal to x
print(numbers)

numbers.insert(2,81)
print(numbers)