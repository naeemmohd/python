### What is Python and Why:
  * Open source programming language
  * Interpreted at run-time(unlike compiled Java, C#, like PHP, Perl)
  * Object oriented( like Java and C#)
  * Precise and interactive( very short and precise commands, thus easy to learn)
  * Yet it is one of the most powerful languages in Big Data ( roughly 55-60% Big data scripts and programs are written in Python followed by Java and others
  * It is portable (can be run on lot of hardware and software platforms)
  * Supports a very broad standard library, modules
  * Dynamic data types, garbage collection, interfaces to all major databases
  * Comes in 2 major versions – Python 2.x (e.g. Python 2.7) and Python 3 – till date most of the Python programs are written in Python 2.x so it is better to learn Python 2.7 first.)
  * One more big thing about Python 2.x is that it can import the features of Python 3 by using ( **from __future__ import <import_module>** syntax, e.g **from __future__ import division** imports division from Python 3. 
    * In Python 2.x if you divide 3/2 you will get answer as 1 as Python 2 performs basic division. 
    * In Python 3, it performs true division , if you divide 3/2 you get 1.5).
    
### Python Setup:
  * Since supported by multiple hardware and software platforms, it can be installed in multiples ways
  * Lets focus Installation on Linux - 
    * Method one – Install Python on Linuc and use Python Shell(command line)
      * Install Python – 
        ```
        yum -y install python27
        ```
      * Create a python script file – 
        ```
        echo “print ‘hello'” > hello.py
        ```
      * Execute the python script – 
        ```
        python hello.py
        ```
      * Check Python version– 
        ```
        python --version
        python -V
        ```  
      * Execute some basic Python commands– 
        ```
        print "Hello from Python"
        print 3/2
        print 3.0/2 
        ```  
    * Method two – Install Jupyter Notebooks – on your local system
      * Install Anaconda(Anaconda installs Python, Jupyter notebooka and required dependencies as a package) from [https://www.anaconda.com/download/](https://www.anaconda.com/download/)
      * It has links for Windows, Linux or Mac installations for Python 2.7 as well as 3.6
      * Lets install Python 2.7 using Windows Installer from [https://repo.continuum.io/archive/Anaconda2-5.0.1-Windows-x86_64.exe](https://repo.continuum.io/archive/Anaconda2-5.0.1-Windows-x86_64.exe). Download and install Anaconda.
      * Anaconda is installed now, verify it by opening Anaconda Navigator, from your Windows Start menu.
      * Click open the “Jupyter notebook“. It will open in the browser locally.
      * In the command box, type the python commands and execute
      
### Python - Numbers and Strings:
  * Python supports dynamic datatypes i.e. the type of a variable is decided by the values it holds.
  * If we assign a variable a="Naeem", then a is a string, if a = "9" then its a number and if a=3.0 then its a float.
  * Login to your Host machine(in my case a CentOS 7 machine)
  * Make a directory "mypython" and go to the directory and type and enter "python" to open python prompt– 
    ```
    mkdir mypython && cd mypython
    python
    ```
  * Now execute the below number operations:
    ```
    from __future__ import print_function # imports Python 3.x print method
    a=5 # assign variables
    b=2
    c=a+b #addition
    print (c)
    c=a-b #subtraction
    print (c)
    c=a*b #multiplication
    print (c)
    c=a/b #division
    print (c)
    c=5**2 #exponentiation/power of
    print (c)
    c=5**(1.0/2) #square root
    print (c)
    c=5**(1.0/3) #cube root
    print (c)
    c= 2 + 5 * 5 - 3 # order of operation i.e 2 + 25 -3 = 27 -3 = 24
    print (c)
    c= (2 + 5) * (5 - 3) # order of operation i.e 7 * 2 = 14
    print (c)
    c= 2 + 5 * 5 - 3 # order of operation i.e 2 + 25 -3 = 27 -3 = 24
    print (c)
    c= (2 + 5) * (5 - 3) # order of operation i.e 7 * 2 = 14
    print (c)
    ```
  * True Division(Python 3.x) vs Basic Division(Python 2.x):
    ```
    print 3/2     # 1
    print 3.0/2   # 1.5
    
    from __future__ import division
    print 3/2     # 1.5
    ```
