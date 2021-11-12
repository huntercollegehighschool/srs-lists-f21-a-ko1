'''
*********
PROGRAM 1
*********
Define a function number_of_odds that takes a list of integers as an argument. The function returns how an integer, how many odd numbers are in the list.
'''
def number_of_odds(lst):
  count = 0
  for i in lst:
    if i % 2 == 1:
      count += 1
  return count
