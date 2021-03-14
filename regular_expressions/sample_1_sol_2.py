# Regular expressions are mini-language for specifying text patterns. 
# Writing code to do pattern matching without regular expressions is a huge pain.
# Regex strings often use backslashes (like \d), so they are often written using raw strings: r'\d'
# \d is the regex for a numeric digit character.
# Import the re module first.
# Call the re.compile() function to create a regex object.
# Call the regex object's search() method to create a match object.
# Call the match object's group() method to get the matched string.
import re

message = 'Call me 02-7123-4567 tommorow, or at 02-8123-6541 at my office.'

phone_num_regex = re.compile(r'\d\d-\d\d\d\d-\d\d\d\d')
match_object = phone_num_regex.search(message)
print(match_object.group())

number = phone_num_regex.findall(message)
print(number)