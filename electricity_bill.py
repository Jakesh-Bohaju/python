unit = int(input('Enter total unit'))

if unit <= 20:
    print('Charge is : 80')
elif unit <= 200:
    print('Charge is : ', 80 + (unit - 20) * 8)
else:
    print('Charge is : ', 80 + (unit - 200) * 12 + 180 * 8)
