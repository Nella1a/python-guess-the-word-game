
def check_user_input(input,guessed_characters):
    if len(input) > 1:
      return False
    elif input in guessed_characters:
      print("guessed characters:", guessed_characters)
      return False
    else:
      return True

def start_new_game():
    return input("\nPress 'y' to start a new game or 'any key' to end the game: ")

def reveal_letter(guess, orig_word,reveal_letter_in_word):
  index_of_letter = orig_word.find(guess) # get index of letter
  return reveal_letter_in_word.replace(reveal_letter_in_word[index_of_letter],orig_word[index_of_letter],1)
