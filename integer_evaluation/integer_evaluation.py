number = input('Please input an integer.') 
try:
  number = int(number)
  if (number > 20): 
  print('Your input: ' + str(number) + ' > 20') 
  if (number > 10): 
  print('Your input: ' + str(number) + ' > 10') 
  if (number > 0):
  print('Your input: ' + str(number) + ' > 0')
  if (number < 0): 
  print('Your input: ' + str(number) + ' is negative') 
except ValueError as e: 
  print("Your input is not an integer.") 
