from functions import find_indexes, validate_user_input, start_new_game, reveal_letter, hide_current_secret_word

secret_words = ["king", "gold"]
hide_secret_words = secret_words[:]
secret_words_length = len(secret_words)
guessed_characters = []
guess_left = 0
out_of_guesses = False
guessed_char = ""


# hide characters, show only first and last

'''
for word in hide_secret_words:
  index = hide_secret_words.index(word)
  print(index, word)
  hide_secret_words[index] = word
  for count in range(len(word)):
   if count >= 1 and count < len(word) - 1:
      word = word.replace(word[count],"_",1)
  hide_secret_words[index] = word
'''

start_game = start_new_game()
i = 0
while start_game == 'y':
  guess_count = 3
  guessed_characters = []
  guessed_word = ""
  secret_word = hide_current_secret_word(secret_words[0])
  print(secret_words[0])
  print(secret_word)

  while guess_count and secret_words[0] != guessed_word:
    print(f"\nSecret word: {secret_word} ")
    user_input = input(f"{guess_count} try/tries left.\nYour guess: ")
    valid_input = validate_user_input(user_input)
    guess_count = 0

    if valid_input:

      if user_input in secret_words[i]:
        count = 1
        secret_word = list(secret_word)
        count_char = find_indexes(secret_words[i],user_input)

        for i in count_char:
          secret_word[i] = user_input
          print("reveal secret word", secret_word)
          count += 1
      else:
        print("Upps, wrong guess")
        pass

      guess_count -= 1

    guessed_word = str(guessed_word)
  start_game = start_game()



  #start_game == 'n'
  #print("End of game!")
  #break





'''
start_game = start_new_game()
i = 0

while start_game == 'y' and i < len(hide_secret_word):

  guess_count = 3
  guessed_characters = []

  # check secret words array
  if i < len(hide_secret_word):
    orig_word = secret_words[i]
    guessed_word = hide_secret_word[i]

    while guess_count > no_guess_left and orig_word != guessed_word:
      print(f"\nSecret word: {guessed_word} ")

      user_input = input(f"{guess_count} try/tries left.\nYour guess: ")

      # valid_input = check_user_input(user_input, guessed_characters)

      valid_input = validate_user_input(user_input)
      print("valid input:", valid_input)

      if valid_input:
        if check_user_input_in_secret_word(valid_input,orig_word):

          #guessed_characters.append(user_input)

          #if user_input in orig_word:
            guessed_word = reveal_letter(user_input, orig_word, guessed_word)
            if guessed_word == orig_word:
              print(f"*** {user_input} is correct: {guessed_word} *** ")
              print(f"**** Great work! The secret word is: {guessed_word} ****\n")
            else:
              print(f"*** {user_input} is correct: {guessed_word} *** ")
        else:
            print("Upps.Wrong guess or already guessed!")
            if guess_count == (no_guess_left + 1) and orig_word != guessed_word:
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
  elif i == len(hide_secret_word) - 1:
    print("You have guessed all secret words correctly.")
    break
  else:
    start_game = start_new_game()
    i += 1
'''