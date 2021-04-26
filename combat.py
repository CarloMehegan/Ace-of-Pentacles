from adventurelib import *

#by default, cannot fight
Room.can_attack = False
dungeon.can_attack = True

@when("equip THING")
def attack(thing):
    say(f"{thing} is now your weapon.")

@when("attack THING")
def attack(thing):
    if current_room.can_attack:
        say(f"you attack the {thing}.")
    else:
        say("you cannot fight here")