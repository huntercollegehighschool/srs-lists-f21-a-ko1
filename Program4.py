'''
*********
PROGRAM 4
*********
Define a function above_average that takes a list of integers or floats as an argument. The function will identify the mean of the list, identify the numbers in the list that are greater than the mean, and then return those numbers in a list.

You may define a separate function that finds the average of a list, though you don't have to.
'''
def above_average(lst):
  new_list = []
  average = sum(lst)/len(lst)
  for i in lst:
    if i > average:
      new_list.append(i)
  return sorted(new_list)
  
