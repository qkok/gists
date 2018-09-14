def get_chunks(message, length):
  """Takes a message and breaks it into chunks of a given length.
  Chunks may not exceed the length and words can't be broken up.

  Args:
    message (string): The message to break into chnuks
    length (int): The max length of a chunk

  Returns:
    A list of chunks
  """

  # splits the message on spaces
  exploded_message = message.split()
  new_message = []
  count = 0

  for current_message in exploded_message:
    # a word exceeds the minimum length for a chunk
    if len(current_message) > length:
        return -1

    # test whether a chunk already exists to be added on to
    try:
      if new_message[count]:
        record_exists = True
    except IndexError:
      record_exists = False

    # creates a new chunk
    if not record_exists and len(current_message) <= length:
      new_message.append(current_message)
    # adds another word to a chunk
    elif record_exists and len(new_message[count] + ' ' + current_message) <= length:
      new_message[count] += ' ' + current_message
    # ends a chunk
    else:
      count += 1
      new_message.append(current_message)

  return new_message

message = input('Message: ')
valid_input = False

while not valid_input:
  try:
    length = int(input('Length: '))
    valid_input = True
  except ValueError:
    print('Invalid length')

result = get_chunks(message, length)

if result == -1:
  print('A word exceeded the the given length')
else:
  print('Text chunks: ', result)