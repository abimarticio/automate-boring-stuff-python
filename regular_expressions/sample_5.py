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