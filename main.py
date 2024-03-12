#Step 1 
import random
from hangman import stages
words = ["apple", "banana", "grape", "kiwi", "orange"]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.

choice = random.choice(words)
# print(choice)
  #TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

  
  #TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
found = False 
lives = 6
display = []
for letter in choice:
  display.append("_")
print(display)  
while (lives>0) and ("_" in display):
  found = False
  guess = input("Guess a letter: ").lower()
  for l in range(len(choice)):
    if choice[l] == guess:
      display[l] = guess
      found = True 
  if found == False:
    lives = lives - 1
    print(stages[lives])
  if lives == 0:
    end_of_game = True
  print(display)
  print(lives)