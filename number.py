num1 = input('Enter a whole numeral now:')
num2 = input('Put in another whole number please:')

print('The input is' ,type(num1), type(num2))

total = num1 + num2
print ('Total:', total, type(total))

total = int(num1) + int(num2)
print ('Total:', total, type(total))

total = float(num1) + float(num2)
print ('Total:', str(total), type(total))