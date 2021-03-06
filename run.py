from word_list import word_list
import random
from prettytable import PrettyTable



WORD_LENGTH = 5
answer1 = random.choice(word_list)
attempts1 = []
attempts2 = []
attempts3 = []
attempts4 = []
attempts1.clear()
attempts2.clear()
attempts3.clear()
attempts4.clear()
guess_1 = 0
guess_2 = 0
guess_3 = 0
guess_4 = 0
complete_guess = True
table = PrettyTable()


def guess_match(theanswer, theguess):
  count = 0
  clue = ''
  for letter in theguess:
    if letter == theanswer[count]:
      clue += letter.upper() + ' '
    elif letter in theanswer:
      clue += letter.lower() + ' '
    else:
      clue += (letter + '\u0336') + ' '
    count += 1
  return clue


def num_of_attempts(challenge):
  if challenge == '1':
    return 6
  elif challenge == '2':
    return 7
  elif challenge == '3':
    return 8
  else:
    return 6

def restart_game():
  restart = input('Would you like to play again. Y or N')
  global start_game, play_game, attempts1, attempts2, attempts3, attempts4
  if restart.lower() == 'n':
    start_game = False
    play_game = False
  else:
    play_game = False
    attempts1.clear()
    attempts2.clear()
    attempts3.clear()
    attempts4.clear()


start_game = True
play_game = False
while start_game == True:
  answer1 = random.choice(word_list)
  answer2 = random.choice(word_list)
  if answer2 == answer1:
    answer2 = random.choice(word_list)
  answer3 = random.choice(word_list)
  if answer3 == answer2:
    answer3 = random.choice(word_list)
  answer4 = random.choice(word_list)
  if answer4 == answer3:
    answer4 = random.choice(word_list)
  start = input('Press 1 to learn how to play, press 2 to choose difficulty: \n')
  if start == '1':
    print('Instructions')
  challenge = input("Press 1 for easy mode, 2 for hard mode and 3 for super hard mode: /n")
  max_attempts = num_of_attempts(challenge)
  count = max_attempts + 1
  play_game = True
  while play_game == True:
    table.clear()
    if max_attempts == 0:
      restart_game()
    else:
      remain = count - max_attempts
      print(answer1, answer2, answer3, answer4)
      word = input('Guess a five letter Word: ').lower()
      if len(word) != WORD_LENGTH:
        print('You guess must have five letters')
        complete_guess = False
      else:
        complete_guess = True
      while complete_guess == True:
        if challenge == '2':
          if guess_1 == 1:
            attempts1.append(" ".join(["_"] * WORD_LENGTH))
          else:
            attempts1.append(guess_match(answer1, word))
          if word == answer1:
              guess_1 = 1
          if guess_2 == 1:
            attempts2.append(" ".join(["_"] * WORD_LENGTH))
          else:
            attempts2.append(guess_match(answer2, word))
          if word == answer2:
              guess_2 = 1
          if (guess_1 + guess_2) == 2:
            print('Woo you got both answers')
            print(f'You got it in {remain} guesses')
            guess_1 = 0
            guess_2 = 0
            max_attempts = 0
            restart_game()
          else:
            table.add_column("Hard", attempts1)
            table.add_column('Mode', attempts2)
            print(table)
          complete_guess = False
        elif challenge == '3':
          if guess_1 == 1:
            attempts1.append(" ".join(["_"] * WORD_LENGTH))
          else:
            attempts1.append(guess_match(answer1, word))
          if word == answer1:
              guess_1 = 1
          if guess_2 == 1:
            attempts2.append(" ".join(["_"] * WORD_LENGTH))
          else:
            attempts2.append(guess_match(answer2, word))
          if word == answer2:
              guess_2 = 1
          if guess_3 == 1:
            attempts3.append(" ".join(["_"] * WORD_LENGTH))
          else:
            attempts3.append(guess_match(answer3, word))
          if word == answer3:
              guess_3 = 1
          if guess_4 == 1:
            attempts4.append(" ".join(["_"] * WORD_LENGTH))
          else:
            attempts4.append(guess_match(answer4, word))
          if word == answer4:
              guess_4 = 1

          if (guess_1 + guess_2 + guess_3 + guess_4) == 4:
            print('Woo you got all the answers')
            print(f'You got it in {remain} guesses')
            guess_1 = 0
            guess_2 = 0
            guess_3 = 0
            guess_4 = 0
            max_attempts = 0
            play_again = input('Would you like to play again? Y or N')
            if play_again.lower() == 'n':
              start_game = False
              play_game = False
              attempts1.clear()
              attempts2.clear()
              attempts3.clear()
              attempts4.clear()
            else:
              play_game = False
              attempts1.clear()
              attempts2.clear()
              attempts3.clear()
              attempts4.clear()
          complete_guess = False
          table.add_column("Wordle", attempts1)
          table.add_column('Super', attempts2)
          table.add_column("Hard", attempts3)
          table.add_column('Mode', attempts4)
          print(table)
          complete_guess = False
        else:
          attempts1.append(guess_match(answer1, word))
          table.add_column("Wordle", attempts1)
          print(table)
          if word == answer1:
            print("Congratulations you got it.")
            print(f"It only took you {remain} guesses!")
            max_attempts = 0
            restart_game()
          complete_guess = False
        max_attempts -= 1









