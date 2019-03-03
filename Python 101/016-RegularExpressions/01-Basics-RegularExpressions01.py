# create file 01-Basics-RegularExpressions01.py 
# Use - nano 01-Basics-RegularExpressions01.py 

import re
searchwords =['Redis', 'port', 'server']
logdata = 'Redis version=4.0.9, bits=64, pid=1, just started, Redis Running mode=standalone, port=6379.'
for searchword in searchwords:
    print('Searching word: "%s" in log: "%s".' %(searchword, logdata))
    match = re.search(searchword, logdata)
    if(match):
        print('Successfully searched word: "%s", match start: %d, match end: %d' %(searchword, match.start(), match.end()))
    else:
        print('Could not search word: "%s"' %(searchword))

# now execute the file 
# python 01-Basics-RegularExpressions01.py

