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

# using len method and also string formatting
age="39"
print ('Your name has %d characters and you are %d years old' %(len(name), int(age)))

print('Your name in uppercase = ' + name.upper()) # to uppercase
print('Your name in lowercase = ' + name.lower()) # to lowercase
print('Your name in titlecase = ' + name.title()) # to titlecase
