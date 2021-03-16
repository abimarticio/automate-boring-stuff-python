# Regex Dot-Star and the Caret/Dollar Characters
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