#Assigning Different Variables
name = "Penguin"
age = 15
weight = 38.5

# Printing Different Variables and their Data Type
print("original:")
print("Name :", name)
print("Data type of name is",  type(name))
print()

print("age :", age)
print("Data Type of age is", type(name))
print()

print("Weight :", weight)
print("Data type of weight is", type(weight))
print()
print()

#type casting to convert the datatype of variables
print("After type casting....")

age = str(age)
print("age after typecasting: ",age)
print("Data Type of age is", type(age))

weight = int(weight)
print("weight after typecasting: ",weight)
print("Data Type of weight is", type(weight))