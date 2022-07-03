from functions import find_indexes, validate_user_input, start_new_game, hide_current_secret_word

secret_words = ["good", "gold"]
hide_secret_words = secret_words[:]
secret_words_length = len(secret_words)
guessed_characters = []
guess_left = 0
out_of_guesses = False
guessed_char = ""


start_game = start_new_game()
j = 0
while start_game == 'y':
  guess_count = 3
  guessed_characters = []
  guessed_word = ""
  secret_word = hide_current_secret_word(secret_words[j])
  print(secret_words[j])
  print(secret_word)

  while guess_count and secret_words[j] != guessed_word:
    print(f"\nSecret word: {secret_word} ")
    user_input = input(f"{guess_count} try/tries left.\nYour guess: ")
    valid_input = validate_user_input(user_input)

    if valid_input:
      print("secret_words[i]:", secret_words[j])

      if user_input in secret_words[j]:
        secret_word = list(secret_word)
        count_char = find_indexes(secret_words[j],user_input)

        for i in count_char:
          secret_word[i] = user_input
          print("reveal secret word", secret_word)

        if secret_words[j] == "".join(secret_word):
          print("Well Done. ")
          break

      else:
        print("Upps, wrong guess")

    else:
       print("Only single letters allowed!")

    guess_count -= 1

  start_game = start_new_game()
  j += 1