def bin(values, value, low, high):
  """Runs a binary search through a sorted list to find the position
   of a number.

  Args:
    values (list of int): The sorted list of integers
    value (int): The value to search for
    low (int): The lowest index to start the search for
    high (int): The highest point to end the search at

  Returns:
    The index at which the searched value is found; -1 if not found
  """

  # get the mid-point of the list
  # increased by low to compensate for shifting of the lowest point
  mid = low + (high - low) // 2

  # test when out of bounds
  if high >= 0 and low < len(values):
    # value found
    if values[mid] == value:
      return mid
    
    # search 1st half
    if values[mid] > value:
      return bin(values, value, low, mid - 1)

    #search second half
    return bin(values, value, mid + 1, high)

  return - 1

# get the list of values
values = []
value = input('Enter value ([x] to stop): ')

while value != 'x':
  try:
    value = int(value)
    values.append(value)
    value = input('Enter value ([x] to stop): ')
  except ValueError:
    print('Invalid value')
    value = input('Enter value ([x] to stop): ')

# get the search values
valid_input = False

while not valid_input:
  try:
    search = int(input('Search value: '))
    valid_input = True
  except ValueError:
    print('Invalid value')

sorted_values = sorted(values)

print('Sorted list: ', sorted(values))

result = bin(sorted(values), search, 0, len(values))

if result == -1:
  print('Search value not found')
else:
  print('Value found at index: ', result)