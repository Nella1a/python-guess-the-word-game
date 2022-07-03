import re

from numpy import true_divide


def hide_current_secret_word(secret_word):
  '''hide characters of current secret word except first and last'''
  hide_char = secret_word[1:-1]
  hide_char_length = len(secret_word[1:-1])
  secret_word = secret_word[0] + "*" * hide_char_length + secret_word[-1]
  return secret_word



def validate_user_input(input):
  ''' check if users guess is a single character and not a number '''
  if len(input) == 1 and re.search("[a-zA-Z]",input):
    return True
  else:
    print("Only single letters allowed!")
    return False


'''
def check_user_input_in_secret_word(input,orig_word):
  check if guessed charater is in secret word

  if input in orig_word:
    return True
  else:
    return False
'''

def start_new_game():
    return input("\nPress 'y' to start a new game or 'any key' to end the game: ")


def reveal_letter(guess, orig_word,reveal_letter_in_word):
  index_of_letter = orig_word.find(guess) # get index of letter
  return reveal_letter_in_word.replace(reveal_letter_in_word[index_of_letter],orig_word[index_of_letter])
