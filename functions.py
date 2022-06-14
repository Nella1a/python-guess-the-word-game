
def validate_user_input(input):
  ''' check if user_input is a single character and not a number;
      NEXT (1) Check with regEx include special characters
      NEXT (1) Include as a function in a class
  '''
  if len(input) > 1:
      return False
  else:
      return True


def check_user_input_in_secret_word(input,orig_word):
  '''check if guessed charater is in secret word
  '''
  if input in orig_word:
    return True
  else:
    return False





def start_new_game():
    return input("\nPress 'y' to start a new game or 'any key' to end the game: ")


def reveal_letter(guess, orig_word,reveal_letter_in_word):
  index_of_letter = orig_word.find(guess) # get index of letter
  return reveal_letter_in_word.replace(reveal_letter_in_word[index_of_letter],orig_word[index_of_letter],1)
