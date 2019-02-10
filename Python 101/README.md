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
    * Method one – Install Python on Linux and use Python Shell(command line)
      * Install Python – 
        * Check if a previous version of Python is installed 
        ```
        yum -y install python3 #installs default/latest python3
        yum -y upgrade python3.5 #upgrades to default/latest python3
        
        python -V  # checks for default/latest python version 
        python3 -V # checks for default/latest python 3 version
        
        ```
        * Please see screen shot below
        ![Python versions](./images/001-01-CheckVersion.png)
        
      * Setup an alias for Python3(open ~/.bashrc and update with line below) – 
        ```
        ls /usr/bin/python* # first check what versions of Python are installed
        
        nano ~/.bashrc #opens the bash script file in nano editor, now update the file with below line
        
        alias python=python3.x # make sure 3.x is the highest 3.x version you got from ls /usr/bin/python* command
        
        source ~/.bashrc #ensure the basj script is reloaded and the changes are affected without loging out
        
        python -V  # now checks for default/latest python 3 version 
        
        ```
      * Please see screen shot below
        ![Python versions](./images/001-02-SetDefaultVersion.png)
        
      * Create a python script file – 
        ```
        echo "print('HelloWorld')" > 001-HelloWorld.py
        ```
      * Execute the python script – 
        ```
        python 01-HelloWorld.py
        ```
      * Check Python version– 
        ```
        python --version
        python -V
        ```  
      * Please see screen shot below
        ![Python versions](./images/001-03-HelloWorld.png)
        
      * Execute some basic Python commands– 
        ```
        print "Hello from Python"
        print 3/2
        print 3.0/2 
        ```  
    * Method two – Install Jupyter Notebooks – on your local system
      * Install Anaconda(Anaconda installs Python, Jupyter notebooka and required dependencies as a package) from [https://www.anaconda.com/download/](https://www.anaconda.com/download/)
      * It has links for Windows, Linux or Mac installations for Python 2.7 as well as 3.6
      * Lets install Python 3.6 using Windows Installer from [https://repo.anaconda.com/archive/Anaconda3-2018.12-Windows-x86_64.exe](https://repo.anaconda.com/archive/Anaconda3-2018.12-Windows-x86_64.exe). Download and install Anaconda.
      * Anaconda is installed now, verify it by opening Anaconda Navigator, from your Windows Start menu.
      * Click open the “Jupyter notebook“. It will open in the browser locally.
      * In the command box, type the python commands and execute
      
### Python - Numbers and Strings:
  * Python supports dynamic datatypes i.e. the type of a variable is decided by the values it holds.
  * If we assign a variable a="Naeem", then a is a string, if a = "9" then its a number and if a=3.0 then its a float.
  * Login to your Host machine(in my case a CentOS 7 machine)
  * Make a directory "mypython" and go to the directory and type and enter "python" to open python prompt– 
    ```
    mkdir 'Python 02' 
    cd 'Python 02'
    ```
  * Create a file - 002-Basics.py - save and execute to check and verify the below basic operations:
    ```
    nano 002-Basics.py # create the file
    
    # copy the content below and paste into the nano editor and save
    from __future__ import print_function # imports Python 3.x print method
    
    a=5 # assign variable a
    b=2 # assign variable b
    
    c=a+b #addition
    print ('a=5, b=2, c=a+b #addition = ' + c)
    
    c=a-b #subtraction
    print ('a=5, b=2, c=a-b #subtraction = ' + c)
    
    c=a*b #multiplication
    print ('a=5, b=2, c=a*b #multiplication = ' + c)
    
    c=a/b #division
    print ('a=5, b=2, c=a/b #division = ' + c)
    
    c=a**2 #exponentiation/powerof/cube etc
    print ('a=5, c=a**2 #exponentiation/powerof/square/cube etc = ' + c)
    
    c=a**3 #exponentiation/powerof/square etc
    print ('a=5, c=a**3 #exponentiation/powerof/square etc = ' + c)
    
    c=a**(1.0/2) #square root
    print ('a=5, c=a**(1.0/2) #square root = ' + c)
    
    c=a**(1.0/3) #cube root
    print ('a=5, c=a**(1.0/3) #cube root = ' + c)
    
    c= 2 + 5 * 5 - 3 # order of operation i.e 2 + 25 -3 = 27 -3 = 24
    
    print ('c= 2 + 5 * 5 - 3 # order of operation i.e 2 + 25 -3 = 27 -3 = 24 = ' + c)
    
    c= (2 + 5) * (5 - 3) # order of operation i.e 7 * 2 = 14
    print (c= (2 + 5) * (5 - 3) # order of operation i.e 7 * 2 = 14 = ' + c)
    
    c= 2 + 5 * 5 - 3 # order of operation i.e 2 + 25 -3 = 27 -3 = 24
    print ('c= 2 + 5 * 5 - 3 # order of operation i.e 2 + 25 -3 = 27 -3 = 24 = ' + c)
    
    c= (2 + 5) * (5 - 3) # order of operation i.e 7 * 2 = 14
    print ('c= (2 + 5) * (5 - 3) # order of operation i.e 7 * 2 = 14 = ' + c)
    
    # now execute the file using python 002-Basics.py
    python 002-Basics.py
    
    ```
  * Please see screen shot below
        ![Python Basics](./images/001-04-Basics.png)
        
  * True Division(Python 3.x) vs Basic Division(Python 2.x):
    ```
    print 3/2     # 1
    print 3.0/2   # 1.5
    
    from __future__ import division
    print 3/2     # 1.5
    ```
