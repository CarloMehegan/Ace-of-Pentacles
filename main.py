from adventurelib import *
from puzzle import * # xander's puzzle system
from item import * # micah's level system

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

start()
