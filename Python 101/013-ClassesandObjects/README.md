### Python - Classes and Objects:
  * Create a file - 01-Basics-ClassesandObjects.py:
    * class is blue print of a behavior
    * object is a instance of a class
    * a class has attributes and methods.
    * attributes are the characteristics of a class
    * methods are the operations performed by the classs
    
    ```
    nano 01-Basics-ClassesandObjects.py # create the file
    
    # Example 1 - simplest class definition -, Product is an object of type object 
    #definition of class
    class Product(object):
        pass
    #initialization of class      
    product = Product()
    type(product)
    
    # create a Student class with special method __init__ , __str__, __len__, __del__ and __new__
    class Student(object):
        # __new__ creates a new instance of the class
        def __new__(cls,name,age):
            obj =super().__new__(cls)
            obj.name=name
            obj.age=age
            return obj
        # __init__ initializes a created class
        def __init__(self,name,age):
            self.name=name
            self.age=age
        # __str__ returns the string representation of the object
        def __str__(self):
            return "Name: %s and Age: %d" %(self.name,self.age)
        # __len__ returns the length of the object
        def __len__(self):
            return self.age
        # __del__ destroys an object
        def __del__(self):
            print("Student deleted")
            
    objStud1 = Student(name="Naeem", age=35)  
    print objStud1
    print len(objStud1)
    del objStud1
    
    # now execute the file 
    python 01-Basics-ClassesandObjects.py
    
    ```
  * Please see screen shot below
        ![Python Basics Classes and Objects](../images/001-013-Basics-ClassesandObjects.png)
