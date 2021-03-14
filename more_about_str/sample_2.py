# String Methods
# upper() and lower() return an uppercase or lowercase string.
# isupper(), islower(), isalpha(), isalnum(), isdecimal(), isspace(), istitle() returns True or False if the string is that uppercase, lowercase, alphabetical letters, and so on.
# startswith() and endswith() also return bools.
# ‘,'.join([‘cat', ‘dog']) returns a string that combines the strings in the given list.
# ‘Hello world'.split() returns a list of strings split from the string it's called on.
# rjust() ,ljust(), center() returns a string padded with spaces.
# strip(), rstrip(), lstrip() returns a string with whitespace stripped off the sides.
# replace() will replace all occurrences of the first string argument with the second string argument.
# Pyperclip has copy() and paste() functions for getting and putting strings on the clipboard.

text = 'hello'
print(text.upper()) # HELLO
print(text.lower()) # hello
print(text.isupper()) # False
print(text.islower()) #T rue
print()

print(text.upper().isupper()) # True
print(text.lower().isupper()) # False
print()

print(text.isalpha()) # True
print(text.isalnum()) # True 
print() 

text = 'hello123'
print(text.isalpha()) # False
print(text.isalnum()) # True
print(text.isdecimal()) # False
print()

text = 'Hello world'
print(text.isspace()) # False
print(text[5].isspace()) # True
print(text.istitle()) # False
print(text.title()) # Hello World
print()

text = 'This Is Title Case'
print(text.istitle()) # True
print(text.startswith('This')) # True
print(text.startswith('T')) # True
print(text.startswith('his')) # False
print(text.endswith('Case')) # True
print(text.endswith('e')) # True
print(text.endswith('Cas')) # False
print()

print(','.join(['cats', 'bats', 'rats'])) # cats,bats,rats
print(''.join(['cats', 'bats', 'rats'])) # catsbatsrats
print(' '.join(['cats', 'bats', 'rats'])) # cats bats rats
print('\n\n'.join(['cats', 'bats', 'rats']))
print()

print(text.split()) # ['This', 'Is', 'Title', 'Case']
print(text.split('i')) # ['Th', 's Is T', 'tle Case']
print()

text = 'hello'
print(text.ljust(15)) # hello
print(len(text.ljust(15))) # 15
print(text.rjust(15)) #           hello
print(text.ljust(15, '*')) # hello**********
print(len(text.ljust(15, '*'))) # 15
print(text.rjust(15, '*')) # **********hello
print(text.center(20, '-')) # -------hello--------
print('wekjfgbskjdvns'.center(20, '-'))
print()

text = '    hello world  '
print(text.strip()) # hello world

text = '****hello world**'
print(text.strip('*')) # hello world
print(text.rstrip('*')) # ****hello world
print(text.lstrip('*')) # hello world**     
print(text.replace('*', '=')) # ====hello world== 

