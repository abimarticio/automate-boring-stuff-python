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