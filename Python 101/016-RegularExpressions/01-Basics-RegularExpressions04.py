# create file 01-Basics-RegularExpressions04.py 
# Use - nano 01-Basics-RegularExpressions04.py 


import re
#use match - searches from begining if not specified otherwise
pattern = re.compile('ell')
print(pattern.match('hello world'))        # searches from begining, so not matched
print(pattern.match('hello world', 1))     # searches from nth index, so matched
#use search anywhere
print(pattern.search('hello world'))       # searches anywhere, so matched
print(pattern.search('hello world', 1))    # searches from 1st index, so matched
print(pattern.search('hello world', 2))    # searches from 2nd index, so not matched

# searchh and replace using re.sub
string1 = "23fs428\634iuo923 . 32'';423[4jfds 8932ds hisdf9f hs80823"

result = re.sub(r'\D', "", string1)
print(result)

result = re.sub(r'\D', " ", string1)
print(result)

result = re.sub(r'\D', ".", string1)
print(result)

# Advanced searching 
string1 = "Hello world is awesome"
# searches words before (.*) and after (.*?) a word here 'world'
# search is re.M means multiline and search is re.I(Ignorecase)
result = re.search(r'(.*) world (.*?) .*', string1, re.M|re.I)

if (result):
  print(result.group())    # shows whole string
  print(result.group(1))   # showsbefore string
  print(result.group(2))   # shows after string
else:
  print("No result")

# now execute the file 
# python 01-Basics-RegularExpressions04.py

