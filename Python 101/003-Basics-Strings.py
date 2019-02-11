name="Mohd Naeem" # assign variable name with value 'Naeem'

# using string variable
print ('Your name is(using string variable):' +  name)
print ('Your name is(using sequence):' +  name[:])

# string variable is a sequence of characters
print ('First letter of your name is  = ' + name[0])
print ('Fifth letter of your name is  = ' + name[4])
print ('Last letter of your name is  = ' + name[:1])
print ('Last 4 letter of your name is  = ' + name[:4])

print ('Your name without first character is  = ' + name[1:])
print ('Your reversed name is  = ' + name[:-1])
print ('Your reversed name by skiiping 2 charatcers is  = ' + name[:-2])

# using len method and also string formatting
age="39"
print ('Your name has %s characters' %(len(name)) %(int(age)))
