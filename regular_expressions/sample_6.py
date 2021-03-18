# Regex sub() and Vebrose Mode

import re

message = 'Agent Alice gave the secret documents to Agent Bob.'
names_regex = re.compile(r'Agent \w+')
match_object = names_regex.findall(message)
print(match_object) # ['Agent Alice', 'Agent Bob']
print(names_regex.sub('REDACTED', message))
# REDACTED gave the secret documents to REDACTED.


names_regex = re.compile(r'Agent (\w)\w*')
match_object = names_regex.findall(message)
print(match_object) # ['A', 'B']
print(names_regex.sub('Agent \1*****', message))
# Agent A***** gave the secret documents to Agent B*****.