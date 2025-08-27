country_code = {'Pakistan' : '0092',
                'Japan' : '0081',
                'Indonesia' : '0062'}

# search dictionary for country code of Pakistan
print("Country code for Pakistan -")
print(country_code.get('Pakistan', 'Not Found'))

print()

# search dictionary for country code of Australia
print("Country code for Australia -")
print(country_code.get('Australia', 'Not Found'))