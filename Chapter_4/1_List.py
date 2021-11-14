# List
#  -  Python list are containers to store a set of values of any data type'
#  -  List can be indexed just like a string

listExAllDataType = [1,"hello",3.4,'''helllo  WORLD''',False]
listEx = [1,2,3,4,5,688,22]

print(listEx)

#List indexing

print("*******************List indexing************")
print("Index 0",listEx[0])
print("Index 5",listEx[5])
listEx[5] = 6 # this will replace the 5th index element


#list Slicing

print("*******************List slicing************")
print("get the 3 element from start",listEx[:3])
print("get the all element from 3",listEx[3:])
