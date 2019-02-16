
# Dictionary: mutable mappings(made up of set of key value pairs) 
# While String is an immutable sequences and lists are mutable sequences,
# Dictionaries are actually mutable mappings,
# Mappings are collection of objects stored as key value pairs.
# initilaize a dictionary
dict = {}
# or initilaize a dictionary with key value pair
dict = {'FL': 'Florida', 'OH':'Ohio'}

# add items to dictionary
dict['TX'] = 'Texas'
dict['NY'] = 'New York'
dict['CA'] = 'California'
print(dict)

# access only keys or only values
print(dict.keys())
print(dict.values())

# view the items of the dictionary
print(dict.items())

# update an item in the dictionary 
dict.update({'OH':'OHIO'})
print(dict)

# pop an item out the dictionary
dict.pop('OH')
print(dict)

# clearing a dictionary 
dict.clear()
print(dict)

# looping a dictionary 
# looping through a dictionary
print(dict)
for k,v in dict.items():
    print('Key: {0} Value: {1}'.format(k, v))
for k in dict.keys():
    print('Key: {0}'.format(k))
for v in dict.values():
    print('Values: {0}'.format(v))

# looping through a dictionary using items() method
for item in dict.items():
    print(item)

# looping through a dictionary using keys() method
for key in dict.keys():
    print(key)

# looping through a dictionary using itervalues() method
for value in dict.values():
    print(value)

# create a nested dictionary with  key value pairs
dict = {'Name': 'Naeem', 'Age': 37, 'Address': {'Address1': '1 Austin St','City': 'Austin','State': 'TX', 'Zip': '78610'}}
print(dict)
print(dict['Name'])
print(dict['Age'])
print(dict['Address'])
print(dict['Address']['Address1'])
print(dict['Address']['City'])
print(dict['Address']['State'])
print(dict['Address']['Zip'])

# deleting dictionaries
del dict["TX"]  # deletes nth key from dictionary
del dict    # deletes entire dictionary
