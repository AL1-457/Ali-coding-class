num = int(input("enter any number and we'll count how many digits are there: "))

count = 0

while num != 0:
    count = count + 1
    num=num//10 #Floor division to get the result without decimal value

print("total digit of the number is = ",count)