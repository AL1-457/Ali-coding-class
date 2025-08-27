def multiple_tuple(num):
    temp = list(nums)
    product = 1

    for x in temp:
        product = product * x

    return product

nums = (4, 3, 2, 2, -1, 18)
print("Original Tuple: ")
print(nums)
print()

result = multiple_tuple(nums)

print("Product - multiplying all the numbers of the said tuple:",result)
print()