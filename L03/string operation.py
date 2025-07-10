#input a word
text = input("Enter a string: ")

#reverse string
#using step value as -1  to iterate in reverse
revText = text[::-1]
text = revText

print(" Reverse of Given string is:")
print(text)

print()

#convert to uppercase
message = "python is fun"
upper = message.upper()
print(upper)