from functions import validate_user_input, start_new_game, reveal_letter, check_user_input_in_secret_word
# variables
# from re import U


# words = [{
#   "level_one": ["king", "gold","vienna","finance","developer"]
# },
# {
#   "level_two": ["king", "gold","vienna","finance","developer"]
# },
# {
#   "level_three": ["king", "gold","vienna","finance","developer"]
# },
# ]

secret_words = ["king", "gold"]

hide_secret_words = secret_words.copy()
word_length = len(secret_words)
guessed_characters = []
no_guess_left = 0
out_of_guesses = False
user_input = ""
i = 0

# hide characters, show only first and last
for word in hide_secret_words:
  index = hide_secret_words.index(word)
  for i in range(len(word)):
   if i >= 1 and i < len(word) - 1:
      word = word.replace(word[i],"_",1)
  hide_secret_words[index] = word





start_game = start_new_game()
i = 0

while start_game == 'y' and i < len(hide_secret_words):

  guess_count = 3
  guessed_characters = []

  # check secret words array
  if i < len(hide_secret_words):
    orig_word = secret_words[i]
    guess_word = hide_secret_words[i]

    while guess_count > no_guess_left and orig_word != guess_word:
      print(f"\nSecret word: {guess_word} ")

      user_input = input(f"{guess_count} try/tries left.\nYour guess: ")

      # valid_input = check_user_input(user_input, guessed_characters)

      valid_input = validate_user_input(user_input)
      print("valid input:", valid_input)


      if check_user_input_in_secret_word(valid_input,guessed_characters):
      #if valid_input:
        guessed_characters.append(user_input)

        if user_input in orig_word:
          guess_word = reveal_letter(user_input, orig_word, guess_word)
          if guess_word == orig_word:
            print(f"*** {user_input} is correct: {guess_word} *** ")
            print(f"**** Great work! The secret word is: {guess_word} ****\n")
          else:
            print(f"*** {user_input} is correct: {guess_word} *** ")
        else:
          print("Upps.Wrong guess or already guessed!")
          if guess_count == (no_guess_left + 1) and orig_word != guess_word:
             out_of_guesses= True
             break
        guess_count -= 1
      else:
        print("Only single letters allowed!")

  if out_of_guesses:
    print(f"Sorry you have no tries left.")
    start_game = start_new_game()
    i = 0
    out_of_guesses= False
  elif i == len(hide_secret_words) - 1:
    print("You have guessed all secret words correctly.")
    break
  else:
    start_game = start_new_game()
    i += 1
