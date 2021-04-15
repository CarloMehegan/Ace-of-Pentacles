from adventurelib import *

@when("exclaim")
def yell():
  print("You bellow at the top of your lungs.")

@when("enter the cave", context='field')
def go_cave():
  set_context('cave')
  print("You enter the cave 2")

@when("exit the cave", context='cave')
def exit_cave():
  set_context('field')
  print("You exit the cave")

@when("take THING")
def take(thing):
  print(f"You take the {thing}.")

@when("look around", context="cave")
def look_cave():
  print("You find yourself in a dark, damp cave.")

@when("look around", context="field")
def look_field():
  print("You find yourself in a bright, sunny field")

set_context('field') # built-in function
start()
