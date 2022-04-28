#first python program for Made
inputs = input("Please enter your own String : ")
lookingfor = input("Please enter your own Character : ")
help_y =input("Please provide value for starting point: ")
i=int(help_y)
newvalue = "";

count = 0
for i in range(len(inputs)):
    if(inputs[i] == lookingfor):
        newvalue = inputs.replace(lookingfor, "cat")
print(newvalue)
