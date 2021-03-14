# Dictionaries are unordered, contain key-value pairs.
# Dictionaries are mutable.
#  Variables hold references to dictionary values, not the dictionary itself.

my_cat = {'size': 'fat', 'color': 'black', 'disposition': 'loud'}
print(my_cat['size']) # fat

cat_1 = {'name': 'Zophie', 'species': 'cat', 'age': 8}
cat_2 = {'species': 'cat', 'age': 8, 'name': 'Zophie'}
print(cat_1 == cat_2) # True


print(cat_1)
print('name' in cat_1) 
print('name' not in cat_1)
print(cat_1.keys())
print()

# to have list like data type
print(list(cat_1.keys()))
print(list(cat_1.values()))
print(list(cat_1.items()))
print()

# loops
for k in cat_1.keys():
    print(k)

for v in cat_1.values():
    print(v)

for k, v in cat_1.items():
    print(k, v)

for i in cat_1.items():
    print(i) # key and value in tuples

print()

# get method takes two arguments 
# first is the key of the values for retrieve
# second is a fallback, default value that the get method returns
# get method can return a default value if a key doesn't exist
print('cat' in cat_1.values())
print(cat_1.get('age', 0))
print(cat_1.get('color', 'black'))
print(cat_1)
print()

# opposite of get method is set default
if 'color' not in cat_1:
    cat_1['color'] = 'black'

cat_1.setdefault('color', 'black')
print(cat_1)
cat_1.setdefault('color', 'orange')
print(cat_1) # still black, color already exist and default value is black

