from adventurelib import *

inv=Bag()
here=Room("""You are in a place""")
here.items = Bag([
 Item("apple"),
])
current_room=here
@when("take the ITEM")
@when("take ITEM")
def take(item):
  object =current_room.items.take(item)
  if not object:
    print(f"There is no {item} here.")
  else:
    inv.add(item)
    print(f"You take the {item}.")
@when("inventory")
def inventory():
  print("Your inventory contains:")
  if not inv:
    print ("nothing")
    return
  for item in inv:
    print (f'{item}')