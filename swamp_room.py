from adventurelib import *

#temporary room for testing combat.py

#create dungeon room
global swamp
swamp = Room("a dark, scary dungeon under the castle")
swamp.can_attack = True

#create enemies in dungeon
swamp.enemies = Bag()
v1 = Item("Vampire")
v1.weakness = "Garlic"
v2 = Item("Shrek")
v2.weakness = "Onion"
swamp.enemies.add(v1)
swamp.enemies.add(v2)

#temporary inventory for testing
inv = Bag()
inv.add(Item("Garlic"))
inv.add(Item("Onion"))

#temporary inventory
@when("inv")
def inv_look():
    for item in inv:
        say(f"{item}")