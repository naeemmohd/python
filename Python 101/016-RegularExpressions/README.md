### Python - Debugging:
  * Regular Expressions
    * used effectively in lot of tasks like data clean up, parsing data, pattern matching
    * Python uses a module ‘re’ for regular expressions
    * How to search : match = **re.match(searchword, searchsource)** returns a boolean
    * How to find location of search : **match.start()** and **match.end()** return the start and end locations of the search
    * How to find all instances of a search word : all = **re.findall(searchword, searchsource)**
    * are used to text matching or parsing
    
  * Create a file - 01-Basics-RegularExpressions01.py:

    
    ```
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
    python 01-Basics-RegularExpressions01.py

    ```
  * Please see screen shot below
        ![Python Basics Regular Expressions](../images/001-016-Basics-RegularExpressions01.png)
        
* Create a file - 01-Basics-RegularExpressions02.py:

    
    ```
    import re
    searchword ='Redis'
    logdata = 'Redis version=4.0.9, bits=64, pid=1, just started, Redis Running mode=standalone, port=6379.'
    match = re.findall(searchword, logdata)
    print(match)
    if(match):
        print('Successfully searched word: "%s"' %(searchword))
    else:
        print('Could not search word: "%s"' %(searchword))
            
    # now execute the file 
    python 01-Basics-RegularExpressions02.py

    ```
  * Please see screen shot below
        ![Python Basics Regular Expressions](../images/001-016-Basics-RegularExpressions02.png)
        
* Create a file - 01-Basics-RegularExpressions03.py:

    
    ```
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
    python 01-Basics-RegularExpressions03.py

    ```
  * Please see screen shot below
        ![Python Basics Regular Expressions](../images/001-016-Basics-RegularExpressions03.png)