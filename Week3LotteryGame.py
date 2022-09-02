import random

print('Welcome to the Lottery Game\n')

print('Your lucky dip numbers for this game are:')

user_numbers = random.sample(range(1, 59), 7)
user_numbers.sort()
print(user_numbers)

print('\n')

print('The lottery numbers for this game are:')
lottery_numbers = random.sample(range(1, 59), 7)
lottery_numbers.sort()
print(lottery_numbers)

print('\n')

matching_numbers = 0
for number in user_numbers:
  if number in lottery_numbers:
  matching_numbers += 1
  
if matching_numbers == 7:
  print('Congratulations! You have won £1000000 for seven matching numbers.')
elif matching_numbers == 6:
  print('Congratulations! You have won £10000 for six matching numbers.')
elif matching_numbers == 5:
  print('Congratulations! You have won £100 for five matching numbers.')
elif matching_numbers == 4:
  print('Congratulations! You have won £40 for four matching numbers.')
elif matching_numbers == 3:
  print('Congratulations! You have won £20 for three matching numbers.')
elif matching_numbers == 2:
  print('You do not have enough matching numbers to win a prize. Better luck next time.')
elif matching_numbers == 1:
  print('You do not have enough matching numbers to win a prize. Better luck next time.')
else:
  print('You have no matching numbers. Better luck next time.')
