# Regex sub() and Verbose Mode
import re


# The sub() regex method will substitute matches with some other text.
# Using \1, \2 and so will substitute group 1, 2, etc in the regex pattern.
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


# Passing re.VERBOSE lets you add whitespace and comments to the regex string passed to re.compile().
# If you want to pass multiple arguments (re.DOTALL , re.IGNORECASE, re.VERBOSE), combine them with the | bitwise operator.
re.compile(r'''
(\d\d-)|    #area code (without parens, with dash)
(\(\d\d\d\)) # -or- area code with parens and dash
\d\d\d\d     # first 4 digits
-            # first dash
\d\d\d\d     # last four digits
\sx\d{2,4}   # extension, like x1234
''', re.IGNORECASE | re.DOTALL | re.VERBOSE)