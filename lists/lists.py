# list is a value that contains multiple values
# values in a list are also called items
# you can access items in a list with it's integer index
# indexes start at 0
# You can get multiple items from list using a slice
# slice has three index (start, end, step)
spam = ['cat', 'bat', 'rat', 'elephant']
print(spam)
# index, single value
print(spam[0])
print(spam[1])
print(spam[3])
# negative indexes
print(spam[-1])
print(spam[-3])
# slice, list value
print(spam[1:3])
print(spam[:])
print(spam[:2])
print(spam[1:])

spam = [['cat', 'bat'], [40, 10, 20, 30]]
print(spam[0])
print(spam[0][0])
print(spam[0][1])
print(spam[1][0])
print(spam[1][2])

# changing list value
spam = [10, 20, 30]
spam[1] = 'hello'
print(spam)
spam[1:3] = ['cat', 'dog', 'mouse']
print(spam)

# del statements
# del statement = "unassignment" statement
spam = ['cat', 'bat', 'rat', 'elephant']
del spam[2]
print(spam)

# string and list similarities
text = 'hello'
print(len(text))
list_text = ['hello', 'rat', 'bat']
print(len(list_text))

print(text + text)
print(list_text + list_text)

print(text * 3)
print(list_text * 3)

text = list('Hello')
print(text)

print('howdy' in ['hello', 'hi', 'howdy'])
print('howdy' not in ['hello', 'hi', 'howdy'])
print()

# for loops
# range() function returns a list like value, which can be passed to the list() function if you need an actual list value
# variables can swap values using multiple assignment
for i in range(4):
    print(i)

print(range(4))

for i in [0, 1, 2, 3]:
    print(i)

print(list(range(4)))
print(list(range(0, 100, 2)))

supplies = ['pens', 'pencils', 'stapler']
for i in range(len(supplies)):
    print(supplies[i], i)

# multiple assignment
cat = ['fat', 'orange', 'loud']
size = cat[0]
color = cat[1]
disposition = cat[2]
print(size)
print(color)
print(disposition)

size, color, disposition = cat
print(size)
print(color)
print(disposition)

# swapping variables
a = 'AAA'
b = 'BBB'
a, b = b, a
print(a)
print()

# methods are functions that are 'called on' values
# index() list method returns the index of an item in the list
# append() list method adds a value to the end of the list
# insert() list method adds a value anywhere inside a list
# remove() list method removes an item, specified by the value, from a list
# sort() list method sort the items in a list
# revese=True keyword argument can sort in reverse order
# sorting happens in "ASCII-betical" order. To sort normally, pass key=str.lower
# these list methods operate on the list "in place", rather than returning a new list value

# index method
spam = ['hello', 'hi', 'howdy', 'heyas', 'hi']
print(spam.index('hello')) # 0
print(spam.index('hi')) # 1

# append method
spam.append('moose')
print(spam)

# insert method
# insert(index, value)
spam.insert(1, 'chicken')
print(spam)

# remove method
spam.remove('hi')
print(spam)

del spam[1]
print(spam)

# sort method
spam = [10, 3, 1, 2, -3]
spam.sort()
print(spam)
spam.sort(reverse=True)
print(spam)

spam = ['a', 'z', 'A', 'Z']
spam.sort()
print(spam)
spam.sort(key=str.lower)
print(spam)
print()

# similarities in list and strings
# strings can do a lot of the same things lists can do, but strings are immutable
# immutable values like strings and tuples cannot be modifies "in place"
# mutable values like lists can be modified in place
# the difference between immutable and mutable comes up with "references"
# variable don't contain lists, they contain references to lists
# when passing a list argument to a function, you are actually passing a list reference
# changes to a list in a function will affect the list outside the function
# deepcopy() function makes a total copy of the list so it doesn't copy the reference to the list

name = 'Zophie'
print(name[0])

for letter in name:
    print(letter)

# creating new string using slice
name = 'Zophie a cat'
new_name = name[:7] + 'the' + name[8:]
print(new_name)
print()

# References
spam = 42
cheese = spam
spam = 100
print(spam)
print(cheese)

spam = [0, 1, 2, 3, 4]
cheese = spam
cheese[1] = 'hello'
print(cheese) # [0, 'hello', 2, 3, 4]
print(spam) # [0, 'hello', 2, 3, 4]

def eggs(someParameter):
    someParameter.append('hello')

spam = [1, 2, 3]
eggs(spam)
print(spam)

# the copy deepcopy() function
import copy
spam = ['A', 'B', 'C']
cheese = copy.deepcopy(spam)
cheese[1] = 42
print(cheese)
print(spam)

# line continuation \
spam = ['apples',
        'oranges',
        'cats']
print(spam)

print('four score and seven ' + \
    'years ago')