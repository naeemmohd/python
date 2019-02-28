nano 01-Basics-ClassesandObjects01.py # create the file
# inheritance in classes - # the parent or base class it has a area method
class Figure(object):    
    length=0
    width=0
    def __init__(self, length=0, width=0):
        self.length=length
        self.width=width
    def area(self):
        return self.length * self.width

objFigure = Figure()
print (objFigure.area())

objFigure = Figure(length=5, width=7)
print (objFigure.area())

# Rectangle child class of class Figure ....its has perimter method of its own, inherits the area method from parent
class Rectangle(Figure):
    def __init__(self, length, width):
        Figure.__init__(self, length, width)
    def perimeter(self):
        return (2*self.length) * (2*self.width)

objFigure = Rectangle(length=5, width=7)
print(objFigure.area())
print(objFigure.perimeter())

# Sphere child class of class Figure ....its has volume method of its own, inherits the area method from parent
class Cube(Figure):
    height =0
    def __init__(self, length, width, height):
        Figure.__init__(self, length, width)
        self.height=height
    def volume(self):
        return self.length * self.width * self.height

objFigure = Cube(length=5, width=7, height=9)
print(objFigure.area())
print(objFigure.volume())

# Cube child class of class Figure ....its has volume method of its own, inherits the area method from parent
class Cube(Figure):
    height =0
    def __init__(self, length, width, height):
        Figure.__init__(self, length, width)
        self.height=height
    def volume(self):
        return self.length * self.width * self.height

objFigure = Cube(length=5, width=7, height=9)
print(objFigure.area())
print(objFigure.volume())


# now execute the file 
python 01-Basics-ClassesandObjects02.py