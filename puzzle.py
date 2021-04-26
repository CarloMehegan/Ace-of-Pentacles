from adventurelib import *
@when("awake")
def wake():
  print("you awaken in strange a room.")

@when("look")
def seeing():
  print("You look at your surroundings.")

@when("letter")
def letter():
  print(" the first thing you see is a letter .")

@when("read")
def read():
  print(" the letter states in order to leave the room you need to solve a riddle.")

@when("hint")
def hints():
  print("it is an object that most people use after dinner .")


@when("riddle")
def riddle():
  print(" the letter states in order to leave the room you need to solve a riddle.")



@when("the answer is ANSWER")
def solve(answer):
  if answer == 'sponge':
    print("A door opens you have answerd correctly .")
  else:
    print("that answer is wrong")
  
@when("riddle")
def riddle():
  print(" the letter states in order to leave the room you need to solve a riddle.")
