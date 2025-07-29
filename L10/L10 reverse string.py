#Input a word or sentence
string = input("please enter your own string : ")

reverse = ""

#loop for printing in reverse
for i in string:
    reverse = i + reverse

print()

print("The original string = ", string)
print("The reversed string = ", reverse)