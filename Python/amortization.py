def calc_payment(initial_amount, interest, number_of_payments):
  """Calculates the loam payment amount assuming interest is 
  compounded per year

  Args:
    initial_amount (float): The initial loan amount
    interest (float): The percentage value of interest per year
    number_of_payments (int): The amount of payments to be made

  Returns:
    The value of the payment to be made
  """
  interest = interest / 100 / 12
  return initial_amount * (interest * ((1 + interest) ** number_of_payments)) / ((1 + interest) ** number_of_payments - 1)

def calc_full_payment(payment_amount, number_of_payments):
  """Calculates the amount to be paid in full

  Args:
    payment_amount (float): The value of the payment to be made
    number_of_payments (int): The amount of payments to be made

  Returns:
    The full amount to be paid
  """
  return payment_amount * number_of_payments

def calc_interest_amount(full_payment, initial_amount):
  """Calculates the amount of interest to be paid

  Args:
    full_payment (float): The full amount to be paid
    initial_amount (float): The initial loan amount

  Returns:
    The amount of interest to be paid
  """
  return full_payment - initial_amount

def exists(var_name):
  """Determines whether a variable has been declared

  Args:
    var_name (string): The name of the variable

  Returns:
    Whether or not the variable has been declared
  """
  return var_name in globals()

valid_input = False

while not valid_input:
  try:
    if not exists('initial_amount'):
      initial_amount = float(input('Initial amount: '))

    if not exists('interest'):
      interest = float(input('Interest rate per year: '))

    if not exists('number_of_payments'):
      number_of_payments = int(input('Number of payments: '))

    valid_input = True
  except ValueError:
    print('Invalid value')

payment_amount = calc_payment(initial_amount, interest, number_of_payments)
full_payment = calc_full_payment(payment_amount, number_of_payments)
interest_amount = calc_interest_amount(full_payment, initial_amount)

print("Loan amount: ", payment_amount)
print("Full amount to be paid: ", full_payment)
print("Interest to be paid: ", interest_amount)
