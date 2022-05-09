
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
characters = []
guess_count = 0
guess_limit = 3
out_of_guesses = False
user_input = ""
i = 0

# hide letters, show only first and last
for word in hide_secret_words:
  index = hide_secret_words.index(word)
  for i in range(len(word)):
   if i >= 1 and i < len(word) - 1:
      word = word.replace(word[i],"_",1)
  hide_secret_words[index] = word

# print(hide_secret_words)

print(f"Try to guess the world as quickly as possible.\nYou have a maximum of 3 tries to guess the word.")

# press y to start the game
# check index of current word
# check if max of 3 tries not exceeded
# Get user input, check character and get index of character
# Stop round: guess is correct or maximum of 3 tries is exceeded
# Start new round (press y) or stop game (press x)
start_game = input("Press 'y' to start the game: ")
i = 0

while start_game == 'y' and i < len(hide_secret_words):
  print("Guess the word:", hide_secret_words[i])
  guess_count = 0
  if i < len(hide_secret_words):
    while guess_count < guess_limit and hide_secret_words[i] != secret_words[i]:
      user_input = input(f"\nYou have {guess_count} tries left.\nYour guess: ")



      index_of_character = secret_words[i].find(user_input) # return = index of the character
      if index_of_character != -1:
        orig_word = secret_words[i]
        guess_word = hide_secret_words[i]
        hide_secret_words[i] = guess_word.replace(guess_word[index_of_character],orig_word[index_of_character],1)
        print(f"{user_input} is correct: {hide_secret_words[i]}")
        if hide_secret_words[i] == secret_words[i]:
          print(f"\nGreat work:  {hide_secret_words[i]}")
          start_game = input("Press 'y' to start a new game or 'x' to end the game: \n")
          break
      elif guess_count == 3 and hide_secret_words[i] != secret_words[i]:
          print("Upps: U could not find the word: \n")
          break
      else:
        print("Upps: wrong guess! Try again.")

      guess_count += 1
    i += 1
  else:
    print("Game Over. There are no words left")
    break

  start_game = input("Press 'y' to start a new game or 'x' to end the game.")

print("GAME OVER")
