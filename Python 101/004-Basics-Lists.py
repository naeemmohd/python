# Lists
# Lists are mutable sequences(recall we said Strings were immutable sequences)

lst = [1,2,3.0,'4','Five']

# entire list 
print(lst)
# length of a list 
print(len(lst))

# list doubled by either lst + lst or lst *2 but you cant mumtiply entire list lst * lst
print(lst + lst)
print(lst * 2)



# list indices - all except first only(not zeroth element)
# one specific index of the list - #e.g first element
print(lst[0])
# range of indices/multiple indices of the list 
print(lst[0:2])

# all except the 0th element
print(lst[1:]) 
#all except the last element
print(lst[:1]) 

# list indices - all elements from 3rd index
print(lst[3:]) 
# list indices - all begining to upto 3rd
print(lst[:3]) 	
# list indices - all except first
print(lst[1::]) 

# list indices - all
print(lst[::1]) 
# list indices - reversed list
print(lst[::-1]) 
# reverse the list by steps of 2
print(lst[::-2])

# add more to list 
print(lst + [6,7.0,'Eight'])
# add more to list using append method
lst.append(6)
lst.append(7.0)
lst.append('Eight')
print(lst)


# pop and sort methods
lst = [5,2,8,3,1,6,4,7]
# sort list
lst.sort()
print(lst)
# pop out last item
print(lst.pop())
# pop out item at nth index
print(lst.pop(3))

#accessing non available index
print(lst[100]) #  this line will give error IndexError