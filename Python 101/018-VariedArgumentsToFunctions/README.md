### Python - Misc. Functions:
  * *args in python is used to pass varied number of arguments to a function
  * **kwargs in python is used to pass varied number of key-value paired arguments to a function

  * Create a file - 01-Basics-VariedArgumentsToFunctions.py - Misc. Functions:
    
    ```
    # create file 01-Basics-VariedArgumentsToFunctions.py by using nano 01-Basics-VariedArgumentsToFunctions.py 

    # *args in python is used to pass varied number of arguments to a function
    # * means zero to n number of arguments
    # Example 1 - passing zero to n number of arguments
    def addAll(*args):
        return sum(args)
    print(addAll()) # 0 arguments
    print(addAll(30,50,80)) # n number of arguments arguments

    #Example 2 - passing zero to n number of arguments along with fixed variable name too
    def addAllNew(arg1, *args):
        return '{} is {}'.format(arg1, sum(args)) 
    print(addAllNew('The sum is: ')) # 0 arguments
    print(addAllNew('The sum is: ', 30,50,80)) # n number of arguments

    # **kwargs in python is used to pass varied number of key-value paired arguments to a function
    # ** means zero to n number of key-value paired arguments
    # Example 1 - passing zero to n number of key-value paired arguments
    def totalMarks(**kwargs):  
        total =0
        for key, value in kwargs.items():
            total = total + value
        return total
    print(totalMarks()) # 0 key-value paired arguments
    print(totalMarks(Maths= 80, Science= 90)) # n number of key-value paired arguments


    # Example 2 - passing zero to n number of key-value paired arguments along with fixed variable name too
    def totalMarks(arg1, **kwargs):  
        total =0
        for key, value in kwargs.items():
            total = total + value
        return '{} is {}'.format(arg1, total) 
    print(totalMarks('The sum is: ')) # 0 key-value paired arguments
    print(totalMarks('The sum is: ', Maths= 80, Science= 90)) # n number of key-value paired arguments

    # now execute the file 
    # python 01-Basics-VariedArgumentsToFunctions.py
    
    ```
  * Please see screen shot below
        ![Python Basics Misc. Functions 01](../images/001-018-Basics-VariedArgumentsToFunctions.png)