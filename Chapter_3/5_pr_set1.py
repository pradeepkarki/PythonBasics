
# accpet the string from user

name = raw_input("Enter the name\n")
date = raw_input("Enter date\n")
print("Good morning," + name)


#
sample='''Hello <name>

You are selected!!!!

Date : <Date>
'''

print(sample.replace("<name>",name).replace("<Date>",date))