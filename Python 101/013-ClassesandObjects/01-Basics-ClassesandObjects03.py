nano 01-Basics-ClassesandObjects03.py # create the file

# instantiating a circle class with with all special methods
# __init__- intializes an object
# __str__ - returns the string representation of an onject
# __len__ - returns the length/count as the case may be
# __del__ - deletes an object
class Circle(object):
    pi = 3.14
    def __init__(self, rad=1):      # default value for a parameter, if no radiius passed will return default of 1
        self.rad=rad
    def __str__(self):
        return "Circle String representation radius:%s" %str(self.rad)
    def __len__(self):
        return self.rad
    def setCircle(self, rad=1):
         self.rad=rad
    def getArea(self):
         print("Circle area(radius):%s" %str(self.pi*(self.rad)**2))
    def getPerimeter(self):
         print("Circle perimiter(radius):%s" %str(2*self.pi*self.rad))
    def __del__(self):
        print("Circle deleted")

objCircle = Circle()  # no radius passed will take dafault value of 1
print(objCircle)
print("Length or raduis of circle %d:" %(len(objCircle)))
objCircle.getArea()
objCircle.getPerimeter()
del objCircle

objCircle = Circle(5)  # raduis is passed as a value of 5
print(objCircle)
print("Length or raduis of circle %d:" %(len(objCircle)))
objCircle.getArea()
objCircle.getPerimeter()
del objCircle

# create a class Cylinder which takes raduis and height 
# and returns the volume (πr2h) and surface area (2πr2 + 2πrh)
class Cylinder(object):
    pi = 3.14
    def __init__(self, rad=1, height=1):
        self.rad=rad
        self.height=height
    def volume(self):
        return ((self.pi)*((self.rad)**2)*self.height)
    def surfacearea(self):
        return ((2*(self.pi)*(self.rad**2)) + (2*(self.pi)*self.rad*self.height))

objCylinder = Cylinder()
print(objCylinder.volume())
print(objCylinder.surfacearea())

objCylinder = Cylinder(2,3)
print(objCylinder.volume())
print(objCylinder.surfacearea())


# now execute the file 
python 01-Basics-ClassesandObjects03.py
