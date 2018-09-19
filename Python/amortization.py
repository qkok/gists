def calc_payment(initial_amount, interest, number_of_payments):
  interest = interest / 100 / 12
  return initial_amount * (interest * ((1 + interest) ** number_of_payments)) / ((1 + interest) ** number_of_payments - 1)

valid_input = False

while not valid_input:
  try:
    initial_amount = float(input('Initial amount: '))
    interest = float(input('Interest rate per year: '))
    number_of_payments = int(input('Number of payments: '))
    valid_input = True
  except ValueError:
    print('Invalid value')

print(calc_payment(initial_amount, interest, number_of_payments))
