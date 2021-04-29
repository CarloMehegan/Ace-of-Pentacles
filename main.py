from adventurelib import *
from puzzle import * # xander's puzzle system
from item import * # micah's level system

field = Room("a field")
field.enemies = Bag()
f1 = Item("Flower")
f1.weakness = "Fire"
field.enemies.add(f1)

import config
config.current_room = field

import swamp_room
import combat

#swamp is the test room for combat.py
@when("enter the swamp", context='field')
def go_swamp():
  set_context('combat')
  config.current_room = swamp_room.swamp
  print("You enter the swamp.")


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
