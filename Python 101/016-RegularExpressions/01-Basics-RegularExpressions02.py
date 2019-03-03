# create file 01-Basics-RegularExpressions02.py 
# Use - nano 01-Basics-RegularExpressions02.py 

import re
searchword ='Redis'
logdata = 'Redis version=4.0.9, bits=64, pid=1, just started, Redis Running mode=standalone, port=6379.'
match = re.findall(searchword, logdata)
print(match)
if(match):
    print('Successfully searched word: "%s"' %(searchword))
else:
    print('Could not search word: "%s"' %(searchword))r

# now execute the file 
# python 01-Basics-RegularExpressions02.py

