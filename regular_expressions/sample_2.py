# Regex Groups and Pipe character
# Groups are created in regex strings with parentheses.
# The first set of parentheses is group 1, the second is 2, and so on.
# Calling group() or group(0) returns the full matching string, group(1) returns group 1's matching string, and so on.
# Use \( and \) to match literal parentheses in the regex string.
# The | pipe can match one of many possible groups.
import re

message = 'My number is 02-7123-4567'
phone_num_regex = re.compile(r'(\d\d)-(\d\d\d\d-\d\d\d\d)')
match_object = phone_num_regex.search(message)
print(match_object.group())
print(match_object.group(1))
print(match_object.group(2))


message = 'My number is (02) 7123-4567'
phone_num_regex = re.compile(r'\(\d\d\) \d\d\d\d-\d\d\d\d')
match_object = phone_num_regex.search(message)
print(match_object.group())


message = 'Batmobile lost a wheel'
bat_regex = re.compile(r'Bat(man|mobile|copter|bat)')
match_object = bat_regex.search(message)
print(match_object.group())