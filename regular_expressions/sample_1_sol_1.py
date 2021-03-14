def isPhoneNumber(text): # 02-8234-1122
    if len(text) != 12:
        return False # not phone number sized

    for i in range(2):
        if not text[i].isdecimal():
            return False # no area code

    if text[2] and text[7] != '-':
        return False # missing dash

    for i in range(3, 7):
        if not text[i].isdecimal():
            return False # no first 4 digits

    for i in range(9, 12):
        if not text[i].isdecimal():
            return False # no second 4 digits
           
    return True

print(isPhoneNumber('02-8123-4567')) # True
print(isPhoneNumber('0281234567')) # False
print(isPhoneNumber('hello')) # False

message = 'Call me 02-7123-4567 tommorow, or at 02-8123-6541 at my office.'
foundNumber = False
for i in range(len(message)):
    chunk = message[i:i+12]
    if isPhoneNumber(chunk):
        print(f'Phone number found: {chunk}')
        foundNumber = True
if not foundNumber:
    print('Could not find any phone numbers')