'''
*********
PROGRAM 2
*********
Define a function odd_reverse that takes a list as an argument. The function creates a new list containing only the elements in the odd indices (indices 1, 3, 5, ...) and then reverses it. The function returns that list.
'''
def odd_reverse(lst):
  new_list = []
  for i in range(len(lst)):
    if i % 2 == 1:
      new_list.append(lst[i])
  new_list.reverse()
  return new_list

