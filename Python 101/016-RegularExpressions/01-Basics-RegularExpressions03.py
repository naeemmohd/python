# create file 01-Basics-RegularExpressions03.py 
# Use - nano 01-Basics-RegularExpressions03.py 

import re
searchdata =['Redis', 'port', 'server']
logdata = 'Redis version=4.0.9, bits=64, pid=1, just started, Redis Running mode=standalone, port=6379.'

def myfindall(searchwords,searchsource):
    '''
    This function searches the searcwords in search source
    and returns all the matches
    '''
    for searchword in searchwords:
        print('Searching searchword: %r' %(searchword))
        print(re.findall(searchword,searchsource))
        print('\n')
        print(re.search(searchword,searchsource))
    
myfindall(searchdata, logdata)


# now execute the file 
# python 01-Basics-RegularExpressions03.py

