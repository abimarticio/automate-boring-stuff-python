# Regex Character Classes and findall() Method
# The regex method findall() is passed a string, and returns all matches in it, not just the first match.
# If the regex has 0 or 1 group, findall() returns a list of strings.
# If the regex has 2 or more groups, findall() returns a list of tuples of strings.
# \d is a shorthand character class that matches digits.
# \w matches "word characters" (letters, numbers, and the underscore). 
# \s matches whitespace characters (space, tab, newline).
# The uppercase shorthand character classes \D, \W, and \S match charaters that are not digits, word characters, and whitespace.
# You can make your own character classes with square brackets: [aeiou]
# A ^ caret makes it a negative character class, matching anything not in the brackets: [^aeiou]
import re


message = 'My numbers are 02-8123-4567, 02-1234-5678 and 02-8413-9874'
phone_regex = re.compile(r'\d\d-\d\d\d\d-\d\d\d\d')
match_object = phone_regex.findall(message)
print(match_object) # ['02-8123-4567', '02-1234-5678', '02-8413-9874']


phone_regex = re.compile(r'(\d\d)-(\d\d\d\d-\d\d\d\d)')
match_object = phone_regex.findall(message)
print(match_object) # [('02', '8123-4567'), ('02', '1234-5678'), ('02', '8413-9874')]


phone_regex = re.compile(r'((\d\d)-(\d\d\d\d-\d\d\d\d))')
match_object = phone_regex.findall(message)
print(match_object) # [('02-8123-4567', '02', '8123-4567'), ('02-1234-5678', '02', '1234-5678'), ('02-8413-9874', '02', '8413-9874')]


lyrics = '''12 drummers drumming, 11 pipers piping, 10 lords a leaping, 9 ladieas dancing. 
            8 maids a milking, 7 swans a swimming, 6 geese a laying, 5 golden rings, 
            4 calling birds, 3 french hens, 2 turtle doves and 1 partridgein a pear tree'''
xmas_regex = re.compile(r'\d+\s\w+')
match_object = xmas_regex.findall(lyrics)
print(match_object)
# ['12 drummers', '11 pipers', '10 lords', '9 ladieas', '8 maids', '7 swans', '6 geese', '5 golden', '4 calling', '3 french', '2 turtle', '1 partridgein']


message = 'Robocop eats baby food.'
vowel_regex = re.compile(r'[aeiouAEIOU]') # r'(a|e|i|o|u|A|E|I|O|U)'
match_object = vowel_regex.findall(message)
print(match_object) # ['o', 'o', 'o', 'e', 'a', 'a', 'o', 'o']


vowel_regex = re.compile(r'[aeiouAEIOU]{2}') # r'(a|e|i|o|u|A|E|I|O|U)'
match_object = vowel_regex.findall(message)
print(match_object) # ['ea', 'oo']


vowel_regex = re.compile(r'[^aeiouAEIOU]') # r'(a|e|i|o|u|A|E|I|O|U)'
match_object = vowel_regex.findall(message)
print(match_object) # ['R', 'b', 'c', 'p', ' ', 't', 's', ' ', 'b', 'b', 'y', ' ', 'f', 'd', '.']