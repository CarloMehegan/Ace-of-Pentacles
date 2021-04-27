from adventurelib import *

#by default, cannot fight
Room.can_attack = False
#create dungeon room
dungeon = Room("a dark, scary dungeon under the castle")
dungeon.can_attack = True
#set current room to dungeon
current_room = dungeon

#create enemies in dungeon
dungeon.enemies = Bag()
v1 = Item("Vampire")
v1.weakness = "Garlic"
v2 = Item("Shrek")
v2.weakness = "Onion"
dungeon.enemies.add(v1)

#create "hand" to represent equipped item
hand = Bag()

#temporary inventory for testing
inv = Bag()
inv.add(Item("Garlic"))
inv.add(Item("Onion"))

#temporary inventory
@when("inv")
def inv_look():
    for item in inv:
        say(f"{item}")

@when("scan room")
def check():
    #like inventory check, list the enemies
    for enemy in current_room.enemies:
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

@when("attack ENEMY")
def attack(enemy):
    #check if you can fight in this room (false by default)
    if current_room.can_attack:
        #look for the ENEMY inputted
        e = current_room.enemies.find(enemy)
        if e is not None:
            say(f"you attack the {enemy}.")
            #check if the equipped item is the enemy's weakness
            w = hand.find(e.weakness)
            if w is not None:
                say(f"the {enemy} is weak to {e.weakness}. you win!")
                current_room.enemies.take(enemy)
            else:
                say(f"the {enemy} resists the attack.")
        else:
            say(f"there is no {enemy} here.")
    else:
        say("you cannot fight here.")

@when("check ENEMY")
def check(enemy):
    #see if you can fight in this room (may remove)
    if current_room.can_attack:
        say(f"you check the {enemy}.")
        #look for ENEMY inputted, print its weakness
        e = current_room.enemies.find(enemy)
        if e:
            say(f"its weakness is {e.weakness}")
        else:
            say(f"there is no {enemy} here.")
    else:
        say("you cannot check here.")