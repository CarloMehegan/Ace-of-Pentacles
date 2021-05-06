from adventurelib import *
from puzzle import * # xander's puzzle system
from item import * # micah's level system
from room1 import * #An's room1

#test starter room, temporary
field = Room("a field")
field.enemies = Bag()
f1 = Item("Flower")
f1.weakness = "Fire"
field.enemies.add(f1)

#config file stores global variables
#we need to keep track of what room we are in; advlib wont do it for us
import config
config.current_room = field

#carlo's imports
import swamp_room
import combat

#swamp is the test room for combat.py
@when("enter the swamp", context='field')
def go_swamp():
  set_context('combat')
  config.current_room = swamp_room.swamp
  print("You enter the swamp.")

set_context('dark')

start()
  


