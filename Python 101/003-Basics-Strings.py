name="Mohd Naeem" # assign variable name with value 'Naeem'

# using string variable
print ('Your name is(using string variable):' +  name)
print ('Your name is(using sequence):' +  name[:])

# string variable is a sequence of characters
print ('First letter of your name is  = ' + name[0])
print ('Fourth letter of your name is  = ' + name[3])
print ('Last letter of your name is  = ' + name[:1])
print ('Last but one letter of your name is  = ' + name[:-1])
print ('All letters of your name is except last 4  = ' + name[:-4])

print ('Your name without first character is  = ' + name[1:])
print ('Your reversed name is  = ' + name[::-1])
print ('Your reversed name by skiiping 2 charatcers is  = ' + name[::-2])

# **** IMp point - though string are sequences but they are immutable(cant be changes by index)
# print name[0] will return 'M' but name[0]='N' will return error

# using len method and also string formatting
age="39"
print ('Your name has %d characters and you are %d years old' %(len(name), int(age)))

print('Your name in uppercase = ' + name.upper()) # to uppercase
print('Your name in lowercase = ' + name.lower()) # to lowercase
print('Your name in titlecase = ' + name.title()) # to titlecase

print('Your name all but last = ' + name[:-1]) #get all but last — Mohd Naee
print('Your name all but last 5 = ' + name[:-5]) #get all but last 5 — Mohd

print('Your name everything with step of 1 = ' + name[::1]) #get everything with step of 1 — Mohd Naeem
print('Your name everything with step of 2 = ' + name[::2]) #get everything with step of 2 — Mh ae

print('Your name in reverse = ' + name[::-1]) #reverse a string — meeaN dhoM
print('Your name in reverse - step of 2 = ' + name[::-2]) #reverse a string with step of 2 — meeaN dhoM

print("#"*30) # repeat a charcter here repeating ‘#’ 30 times

#print formatting – using {} placeholders – order of variable substituion is not needed
strData = 'My name is {} and I am {} years old.'.format(name,age)
print(strData)
strData = 'My name is {thename} and I am {theage} years old.'.format(thename=name,theage=age)
print(strData)
strData = 'My name is %s and I am %d years old.' %(name,int(age))
print(strData)

mypi = 22.0/7
strData = 'The value of pi - upto 2 decimal places is: %1.2f' %(mypi)
print(strData)
strData = 'The value of pi - upto 5 decimal places is: %1.5f' %(mypi)
print(strData)
strData = 'The value of 100000/3 - upto 5 places of before decimal and 5 places after decimal is: %5.5f' %(100000.0/3)
print(strData)
