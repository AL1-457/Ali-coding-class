# Zip elements of two sets
s1 = {2, 3, 1}
s2 = {'b', 'a', 'c'}
s3 = list(zip(s1, s2))
print(s3)
print()

# Zip into dictionary
stocks = ['reliance', 'ifosys', 'tcs']
prices = [2175, 1127, 2750]

new_dict = {stocks: prices for stocks,
            prices in zip(stocks, prices)}

print(f"{new_dict}")