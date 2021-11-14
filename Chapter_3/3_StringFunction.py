#Different python string functions

test = "this is a test string"
#len()
print("len()")

print(len(test))

#string.endsWith("dfg") - check if the string ends with the char or string true,false
print("************endsWith('')****************")

print(test.endswith('g'))

#string.count("") - check the total number of occurance of a string or char return the count
print("*********count('')*************")
print(test.count('i'))

#Capitalize -capitalize the first letter to uppercase
print("******capitalize()********")
print(test.capitalize())

#Find - Return the index where the string is present
#     - Return the first first there are multiple strings
#     - id string is not found then return the -1
print("************find()***********")
print(test.find("sadfsadf"))

# replace- replace ol with new string
print("**************replace(old,new)************")
print(test.replace("is","xyz"))