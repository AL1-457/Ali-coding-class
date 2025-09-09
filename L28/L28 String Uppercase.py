class IOString():
    # constructor to set default value
    def __init__(self):
        self.str1 = ""

    # method to get input from user
    def get_String (self):
        self.str1 = input("enter String : ")

    #method to perint the string in uppercase
    def print_String(self):
        print("Result is :", self.str1.upper())

# Object creation
str_obj = IOString()

#space Call method
str_obj.get_String()
str_obj.print_String()