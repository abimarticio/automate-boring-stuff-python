# Regex Dot-Star and the Caret/Dollar Characters
# ^ means the string must start with pattern.
# $ means the string must end with the pattern. 
# Both ^ and $ means the entire string must match the entire pattern.
# The . dot is a wildcard; it matches any character except newlines.
# Pass re.DOTALL as the second argument to re.compile() to make the . dot match newlines as well.
# Pass re.I or re.IGNORECASE as the second argument to re.compile() to make the matching case-insensitive.
import re


message = 'Hello there!'
begins_with_hello_Regex = re.compile(r'^Hello')
match_object = begins_with_hello_Regex.search(message)
print(match_object) 
# <re.Match object; span=(0, 5), match='Hello'>

message = 'He said "Hello there!"'
begins_with_hello_Regex = re.compile(r'^Hello')
match_object = begins_with_hello_Regex.search(message)
print(match_object) 
# None

message = 'Hello world!'
ends_with_world_Regex = re.compile(r'world!$')
match_object = ends_with_world_Regex.search(message)
print(match_object) 
# <re.Match object; span=(6, 12), match='world!'>

message = 'Hello world!asdfghjkl'
ends_with_world_Regex = re.compile(r'world!$')
match_object = ends_with_world_Regex.search(message)
print(match_object) 
# None

message = '123456789'
all_digits_Regex = re.compile(r'^\d+$')
match_object = all_digits_Regex.search(message)
print(match_object) 
# <re.Match object; span=(0, 9), match='123456789'>

message = '1234x56789'
all_digits_Regex = re.compile(r'^\d+$')
match_object = all_digits_Regex.search(message)
print(match_object) 
# None

message = 'The cat in the hat sat on the flat mat.'
at_regex = re.compile(r'.at')
match_object = at_regex.findall(message)
print(match_object)
# ['cat', 'hat', 'sat', 'lat', 'mat']

message = 'The cat in the hat sat on the flat mat.'
at_regex = re.compile(r'.{1,2}at')
match_object = at_regex.findall(message)
print(match_object)
# [' cat', ' hat', ' sat', 'flat', ' mat']

message = 'First Name: Al Last Name: Sweigart'
name_Regex = re.compile(r'First Name: (.*) Last Name: (.*)')
match_object = name_Regex.findall(message)
print(match_object)
# [('Al', 'Sweigart')]

serve = '<To serve humans> for dinner.>'
non_greedy = re.compile(r'<(.*?)>')
match_object = non_greedy.findall(serve)
print(match_object)
# ['To serve humans']

greedy = re.compile(r'<(.*)>')
match_object = greedy.findall(serve)
print(match_object)
# ['To serve humans> for dinner.']

prime = 'Serve the public trust.\nProtect the innocent.\nUpload the law.'
print(prime)
dot_star = re.compile(r'.*')
match_object = dot_star.search(prime)
print(match_object)
# <re.Match object; span=(0, 23), match='Serve the public trust.'>

dot_star = re.compile(r'.*', re.DOTALL)
match_object = dot_star.search(prime)
print(match_object)
# <re.Match object; span=(0, 61), match='Serve the public trust.\nProtect the innocent.\nU>

message = 'Al, why does your programming book talk about RobCop so much?'
vowel_Regex = re.compile(r'[aeiou]')
match_object = vowel_Regex.findall(message)
print(match_object)
# ['o', 'e', 'o', 'u', 'o', 'a', 'i', 'o', 'o', 'a', 'a', 'o', 'u', 'o', 'o', 'o', 'u']

message = 'Al, why does your programming book talk about RobCop so much?'
vowel_Regex = re.compile(r'[aeiou]', re.IGNORECASE)
match_object = vowel_Regex.findall(message)
print(match_object)
# ['A', 'o', 'e', 'o', 'u', 'o', 'a', 'i', 'o', 'o', 'a', 'a', 'o', 'u', 'o', 'o', 'o', 'u']
