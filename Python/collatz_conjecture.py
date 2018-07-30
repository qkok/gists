count = 0  # number of iterations

def collatz(num):
  """Runs recursively to get the next number according to the Collatz conjecture.
  
  When the number is even, the next number will be the number divided by 2; when
  the number is uneven, the next number will be the number multiplied by 3 plus 1.

  The conjecture is that no matter the value of num (given num > 0 and int), the 
  sequence will always reach 1.

  Args:
    num (int): The number on which to test the Collatz conjecture

  Returns:
    The number of iterations before proving the Collatz conjecture
  """
  global count
  count += 1

  print('Number #%i: %i' % (count, int(num)))

  rules = {
    0: num / 2,
    1: num * 3 + 1,
  }

  if num > 1:
    collatz(rules[num % 2])

  return count - 1  # the first number does not count as an iteration

input_accepted = False  # only accept positive integer input

while not input_accepted:
  try:
    input_num = int(input('Enter a positive integer to test the Collatz conjecture: '))

    if (input_num < 1):
      raise Exception()

    input_accepted = True
  except:
    print('Invalid input')

"""Print correct form of the word 'iteration'"""
if input_num == 1:
  iteration_string = 'iteration'
else:
  iteration_string = 'iterations'

print('It took %i %s to get to 1' % (collatz(input_num), iteration_string))