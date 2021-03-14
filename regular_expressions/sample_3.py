# Repetition in Regex Patterns and Greedy/Nongreedy Matching
# The ? says the group matches zero or one times.
# The * says the group matches zero or more times.
# The + says the group matches one or more times.
# The curly braces can match a specific number of times.
# The curly braces with two numbers matches a minimum and maximum number of times.
# Leaving out the first or second number in the curly braces says there is no minimum or maximum.
# "Greedy matching" matches the longest string possible, "nongreedy matching" (or "lazy matching") matches the shortest string possible.
# Putting a question mark after the curly braces makes it do a nongreedy/lazy match.
import re

message = 'The adventures of Batman'
bat_regex = re.compile(r'Bat(wo)?man')
match_object = bat_regex.search(message)
print(match_object.group()) #Batman


message = 'The adventures of Batwoman'
match_object = bat_regex.search(message)
print(match_object.group()) # Batwoman


# phone_num = 'My number is 02-7123-4567. Call me tomorrow.'
phone_num = 'My number is 7123-4567. Call me tomorrow.'
phone_regex = re.compile(r'(\d\d-)?\d\d\d\d-\d\d\d\d')
match_object = phone_regex.search(phone_num)
print(match_object.group()) #7123-4567


message = 'The adventures of Batwowowoman'
bat_regex = re.compile(r'Bat(wo)*man')
match_object = bat_regex.search(message)
print(match_object.group()) # Batwowowoman


# message = 'The adventures of Batwoman'
message = 'The adventures of Batwowowoman'
bat_regex = re.compile(r'Bat(wo)+man')
match_object = bat_regex.search(message)
print(match_object.group()) # Batwowowoman


message = 'I learned about +*? regex syntax'
regex = re.compile(r'\+\*\?')
match_object = regex.search(message)
print(match_object.group()) # +*?


message = 'I learned about +*?+*?+*?+*?+*? regex syntax'
regex = re.compile(r'(\+\*\?)+')
match_object = regex.search(message)
print(match_object.group()) # +*?+*?+*?+*?+*?


message = ('He said "HaHaHa"')
ha_regex = re.compile(r'(Ha){3}')
match_object = ha_regex.search(message)
print(match_object.group()) # HaHaHa


message = 'My numbers are 02-8123-4567,1234-5678,02-8413-9874'
phone_regex = re.compile(r'((\d\d-)?\d\d\d\d-\d\d\d\d(,)?){3}')
match_object = phone_regex.search(message)
print(match_object.group()) # 02-8123-4567,1234-5678,02-8413-9874


# message = ('He said "HaHaHa"')
message = ('He said "HaHaHaHaHa"')
ha_regex = re.compile(r'(Ha){3,5}')
match_object = ha_regex.search(message)
print(match_object.group()) # HaHaHaHaHa


message = ('He said "HaHaHaHaHa"')
ha_regex = re.compile(r'(Ha){3,}')
match_object = ha_regex.search(message)
print(match_object.group()) # HaHaHaHaHa

# greedy match
message = '123456789'
digit_regex = re.compile(r'(\d){3,5}')
match_object = digit_regex.search(message)
print(match_object.group()) # 12345


# nongreedy match
message = '123456789'
digit_regex = re.compile(r'(\d){3,5}?')
match_object = digit_regex.search(message)
print(match_object.group()) # 123