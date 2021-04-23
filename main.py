from adventurelib import *
import shop
from abstractions import get_look_command


get_look_command("hallway", "a dusty hallway")
get_look_command("room", "A dark room")

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

@when("take THING")
def take(thing):
  print(f"You take the {thing}.")

@when("look around", context="cave")
def look_cave():
  print("You find yourself in a dark, damp cave.")

@when("look around", context="field")
def look_field():
  print("You find yourself in a bright, field")

start()
