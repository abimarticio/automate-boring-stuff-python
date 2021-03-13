# try and except statements

def div42by(divideBy):
    try:
        return 42 / divideBy
    except ZeroDivisionError:
        print('Error: You tried to divide by zero')

print(div42by(2))
print(div42by(12))
print(div42by(0))
print(div42by(1))

# output
# 21.0
# 3.5
# Error: You tried to divide by zero
# None -> Remember: Functions that return without a return statement return the None value.
# 42.0