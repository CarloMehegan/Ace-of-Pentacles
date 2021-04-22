from adventurelib import *
from item import *
@when("exclaim")
def yell():
  print("You bellow at the top of your lungs.")

@when("enter the cave", context='field')
def go_cave():
  set_context('cave')
  print("You enter the cave")

@when("exit the cave", context='cave')
def exit_cave():
  set_context('field')
  print("You exit the cave")



@when("look around", context="cave")
def look_cave():
  print("You find yourself in a dark, damp cave.")

@when("look around", context="field")
def look_field():
  print("You find yourself in a bright, field")

set_context('field')
start()
