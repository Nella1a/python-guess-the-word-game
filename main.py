
# variables
from re import U


words = ["king", "gold","vienna","finance","developer"]
user_guess = words.copy()
word_length = len(words)
characters = []
count = 3
user_input = ""
i = 0

# show only first and last character of original worlds
for word in user_guess:
  index = user_guess.index(word)
  for i in range(len(word)):
   if i >= 1 and i < len(word) - 1:
      word = word.replace(word[i],"_",1)
  user_guess[index] = word

print(f"Try to guess the world as quickly as possible.\nYou have a maximum of 3 tries to guess the word.")

# press y to start the game
# check index of current word
# check if max of 3 tries not exceeded
# Get user input, check character and get index of character
# Stop round: guess is correct or maximum of 3 tries is exceeded
# Start new round (press y) or stop game (press x)
start_game = input("Press 'y' to start the game: ")
i = 0

while start_game == 'y':
  print("Guess the word:", user_guess[i])
  count = 3
  if i < 5:
    while count >= 1 and user_guess[i] != words[i]:
      user_input = input(f"\nYou have {count} tries left.\nYour guess: ")
      index_of_character = words[i].find(user_input) # return = index of the character
      if index_of_character != -1:
        orig_word = words[i]
        guess_word = user_guess[i]
        user_guess[i] = guess_word.replace(guess_word[index_of_character],orig_word[index_of_character],1)
        print(f"{user_input} is correct: {user_guess[i]}")
        if user_guess[i] == words[i]:
          print(f"\nGreat work:  {user_guess[i]}")
          start_game = input("Press 'y' to start a new game or 'x' to end the game: \n")
          break
      else:
        print("Upps: wrong guess! Try again.")

      count -= 1
    i += 1
  else:
    print("Game Over. There are no words left")
    break

start_game = input("Press 'y' to start a new game or 'x' to end the game.")
