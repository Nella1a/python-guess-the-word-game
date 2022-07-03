import re


def hide_current_secret_word(secret_word):
  '''hide characters of current secret word except first and last'''
  #hide_char = secret_word[1:-1]
  hide_char_length = len(secret_word[1:-1])
  secret_word = secret_word[0] + "*" * hide_char_length + secret_word[-1]
  return secret_word


def validate_user_input(input):
  ''' check if users guess is a single character and not a number '''
  if len(input) == 1 and re.search("[a-zA-Z]",input):
    return True
  else:
    return False


def start_new_game():
    return input("\nPress 'y' to start a new game or 'any key' to end the game: ")


def find_indexes(secr_word, character):
  '''find indexes of guessed character in secret word
  '''
  return [index for index, char in enumerate(secr_word) if char == character]
