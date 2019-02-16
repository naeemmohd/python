# Tuples are also like lists except that they are immutable
# Once created can’t be updated
# We use tuples very extensivly to ensure where the number of elements should be fixed and should not change.
# E.g columsn in a csv or psv file where you would expect fixed number of columns
# lets assume the a csv file with data like this 
# where fixed columns are InvoiceID,CustomerName,Balance,IsProcessed
# 1,'Kelly Bennett',551,0
testTuple = (1,'Kelly Bennett',551,0,1)
print(testTuple)
print(testTuple[0])
print(testTuple[0:2])

# Two methods supported - 
# index(returns the index of an item) and 
# count(returns how many times and items occured in the tuple)
print(testTuple.count(1))
print(testTuple.index(0))

# But Tuples are immutable i.e. can't be modified once created
testTuple[0]=2 # this will be an error as tuples are immutables
print(testTuple)

# make a distict set of the tuple
mytuple = (1, 2, 3, 3, 3, 1, 1,1, 3, 3, 1, 1)
print(set(mytuple))

#delete a tuple item or whole tuple
del mytuple[0] - deletes only nth member
del mytuple - deletes entire tuple


