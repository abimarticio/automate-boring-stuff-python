# Advanced String Syntax
# Strings are enclosed by a pair of single quotes or double quotes (as long as the same kind are used).
# Escape characters let you put quotes and other characters that are hard to type inside strings.
# Raw strings (which have the r prefix before the first quote) will literally print any backslashes in the string and ignore escape characters.
# Multiline strings begin and end with three quotes, and can span multiple lines.
# Indexes, slices, and the "in" and "not in" operators all work with strings.


# escape characthers
# single quote \'
# double quote \"
# new tab \t
# new line \n
# \\ backslash
print("That is Alice's cat")
print('Say hi to Bob\'s mother')
print('hello there!\nHow are you?\nI\'m fine')

# raw string
print(r'Hello')
print(r'That is Carol\'s cat')

print("""Dear Alice,
Eve's cat has been arrested for catnapping, cat burglary and extortion.
Sincerely,
Bob.""")
spam = """Dear Alice,
Eve's cat has been arrested for catnapping, cat burglary and extortion.
Sincerely,
Bob."""
print(spam)

spam = 'Hello world!'
print(spam[0]) # 'H'
print(spam[1:5]) # 'ello'
print(spam[-1]) # '!'

print('Hello' in spam) # True
print('Hello' not in spam) # False