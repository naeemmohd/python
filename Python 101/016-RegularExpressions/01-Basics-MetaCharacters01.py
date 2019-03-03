# create file 01-Basics-RegularExpressions01.py 
# Use - nano 01-Basics-RegularExpressions01.py 

import re
searchsource = 'Za?..pqrs..pppqqq...stttsttt...efef!...Xpxxxx baaaa 123'
searchpatterns = [ 'sd*',       # s followed by zero or more d's
                'sd+',          # s followed by one or more d's
                'sd?',          # s followed by zero or one d's
                'sd{3}',        # s followed by three d's
                'sd{2,3}',      # s followed by two to three d's
                's[sd]+',       # s followed by one or more s or d
                '[sd]',         # either s or d
                '[^!.? ]'       # check for matches that are not a !,.,?, or space
                '[a-z]+',       # sequences of lower case letters
                '[A-Z]+',       # sequences of upper case letters
                '[a-zA-Z]+',    # sequences of lower or upper case letters
                '[A-Z][a-z]+'   # one upper case letter followed by lower case letters
                r'\d+',         # sequence of digits
                r'\D+',         # sequence of non-digits
                r'\s+',         # sequence of whitespace
                r'\S+',         # sequence of non-whitespace
                r'\w+',         # alphanumeric characters
                r'\W+',         # non-alphanumeric
                ]
def myfindall(searchwords,searchsource):
    for searchword in searchwords:
        print('Searching searchword: %r' %(searchword))
        print(re.findall(searchword,searchsource))

myfindall(searchpatterns, searchsource) 
# now execute the file 
# python 0-Basics-RegularExpressions01.py

