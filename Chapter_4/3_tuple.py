#Tuple
# - Tuples are immutable datatype in python I.e you cannot change the value in the tuple 
# - () braces is used to store
# -  if it has single element then add , at the end
t1 = (1,2,3,1)
#tupleEx[1] = 2  # this will throw an error
t2 = () # Empty tuple
#t3 = (1) # wrong way comma is needed if tuple has single element
t4 = (1,) # Tuple with single element   



# Methods
#1.count() -  count the occurance of the element
print(t1.count(1))

#2.index() - get the index of the tuple element
print(t1.index(1))
