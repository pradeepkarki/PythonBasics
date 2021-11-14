

name = "pradeep"
greeting="good morning,"

#conacatinating two strings
print(greeting+name)

#index
print("Char at index 2")
print(name[2])

#name[2]='d' -> python doesnot allow this 

print("print with slicing")
print(name[0:4])
print(name[:4]) # is same as name[0:4] which means get the 4 elements strting from 0
print(name[0:]) # is same as name[0:last_index]

print("print with negative index")
print(name[-5:-1]) #t same as printing name[2:6] last index will be -1

print("Slicing with skip value")
name="pradeepisgood"
print(name[0::1])
print(name[0::2])

