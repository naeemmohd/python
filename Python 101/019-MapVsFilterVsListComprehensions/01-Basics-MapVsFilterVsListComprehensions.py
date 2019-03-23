# create file 01-Basics-MapVsFilterVsListComprehensions.py by using nano 01-Basics-MapVsFilterVsListComprehensions.py

# map function Vs filter functions vs List comprehensions
# map function -  applies a function on iterative list of items
getSquares = lambda x : x**2    # function using lambda expression
print(getSquares(5))            # calling the function 
mylist = list(range(1,6))       # creating a list
print(mylist)
retValues = map(getSquares,mylist) # calling getSquares function on mylist - syntax - map(function, list)
print(list(retValues))

# list comprehensions -  its more pythonic, fast and precise way of creating lists
print([x**2 for x in mylist])
print([x**2 for x in mylist if x%2==0])
print([(x,y) for x in mylist if x%2==0 for y in mylist if y%2==1])

# filter functions applies a function on list of all iterbales but filters only those which return true 
isodd = lambda num : num%2!=0 # the isodd function
retValues = filter(isodd,mylist) # calling isodd function on mylist - syntax - filter(function, list)
print(list(retValues))

!python -mtimeit -s'mylist=range(1,51)' 'map(lambda x : x**2, mylist)' # map function
!python -mtimeit -s'mylist=range(1,51)' 'filter(lambda num : num%2!=0, mylist)' # filter function
!python -mtimeit -s'mylist=range(1,51)' '[x**2 for x in mylist]'  # list comprehension
# simple loop
#import timeit
myloop = """\
mylist = []
for x in range(1,51):
    mylist.append(x)
"""
print((timeit.Timer(stmt=myloop)).timeit())

# now execute the file 
# python 01-Basics-MapVsFilterVsListComprehensions.py