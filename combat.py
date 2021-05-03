from adventurelib import *
import config

#create "hand" to represent equipped item
hand = Bag()

@when("scan enemies", context='combat')
def scan_enemies():
    #like inventory check, list the enemies
    for enemy in config.current_room.enemies:
        say(f"{enemy}")

@when("equip THING")
def equip(thing):
    #sometimes when "thing" doesnt exist it throws an error
    #so just use a try here to catch those
    try:
        #if we have the item, put it in hand and remove from inv
        if thing in inv:
            #put current weapon in inv, but only if hand is not empty
            if hand.get_random() is not None:
                inv.add(hand.take_random())
            hand.add(inv.take(thing))
            say(f"{thing} is now your weapon.")
        else:
            say(f"there is no {thing} in your inventory.")
    except:
        say(f"there is no {thing} in your inventory.")

@when("attack ENEMY", context='combat')
def attack(enemy):
    #look for the ENEMY inputted
    e = config.current_room.enemies.find(enemy)
    if e is not None:
        say(f"you attack the {enemy}.")
        #check if the equipped item is the enemy's weakness
        w = hand.find(e.weakness)
        if w is not None:
            say(f"the {enemy} is weak to {e.weakness} and runs away!")
            config.current_room.enemies.take(enemy)
        else:
            say(f"the {enemy} resists the attack.")
    else:
        say(f"there is no {enemy} here.")

@when("check ENEMY", context='combat')
def check(enemy):
    say(f"you check the {enemy}.")
    #look for ENEMY inputted, print its weakness
    e = config.current_room.enemies.find(enemy)
    if e:
        say(f"its weakness is {e.weakness}!")
    else:
        say(f"there is no {enemy} here.")