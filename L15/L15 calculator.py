def add(P,Q):
    return P + Q #sending or returnning the result

def subtract(P,Q):
    return P - Q

def multiply(P,Q):
    return P * Q

def divide(P,Q):
    return P / Q

print("Please select operation.")
print("a. Add")
print("b. Subtract")
print("c. Multiply")
print("d. Divide")

choice = input("Please enter choice (a/b/c/d): ")

num_1 = int(input("Please enter the the first number: "))
num_2 = int(input("Please enter the the second number: "))
print()

if choice.lower() == 'a': # conver input into lowercase letter and then check if it's 'a' letter
    result = add(num_1,num_2)
    print(num_1, "+", num_2, "=", result)

elif choice.lower()  =='b':
    result = subtract(num_1, num_2)
    print(num_1, "-",num_2, "=", result)

elif choice.lower()  =='c':
    result = multiply(num_1, num_2)
    print(num_1, "*",num_2, "=", result)

elif choice.lower()  =='d':
    result = divide(num_1, num_2)
    print(num_1, "/",num_2, "=", result)

else:
    print("this is invalid input")