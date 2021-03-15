# Regex Character Classes and findall() Method
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