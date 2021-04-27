from adventurelib import *
@when("awake", context='puzzle')
def wake():
  print("you awaken in strange a room.")

@when("look", context='puzzle')
def seeing():
  print("You look at your surroundings.")

@when("letter", context='puzzle')
def letter():
  print(" the first thing you see is a letter .")

@when("read", context='puzzle')
def read():
  print(" the letter states in order to leave the room you need to solve a riddle.")

@when("hint", context='puzzle')
def hints():
  print("it is an object that most people use after dinner .")


@when("riddle", context='puzzle')
def riddle():
  print(" the letter states in order to leave the room you need to solve a riddle.")



@when("the answer is ANSWER", context='puzzle')
def solve(answer):
  if answer == 'sponge':
    print("A door opens you have answerd correctly .")
  else:
    print("that answer is wrong")
  
@when("riddle", context='puzzle')
def riddle():
  print(" the letter states in order to leave the room you need to solve a riddle.")
