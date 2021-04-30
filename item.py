from adventurelib import *


here=Room("""You are in a place""")
here.items = Bag([
 Item("apple"),
])
current_room=here
## command to create look around commands for rooms with associated bags.
def get_look(description):
  @when("look around")
  def look():
    print(description)
    print("In this area there is:")
    if len(current_room.items)>0:
      for item in current_room.items:
        print(f'{item}')
    else:
      print("Nothing")
## Overarching inventory function
def load_inventory():
  inv=Bag()

  ##place item in room bag into inventory bag
  @when("take the ITEM")
  @when("take ITEM")
  def take(item):
    object =current_room.items.take(item)
    if not object:
      print(f"There is no {item} here.")
    else:
      inv.add(item)
      print(f"You take the {item}.")
##list inventory bag
  @when("inventory")
  def inventory():
    print("Your inventory contains:")
    if not inv:
      print ("nothing")
      return
    for item in inv:
      print (f'{item}')

def create_room(name,description,bag):
  ##create a room contaiining a bag of items and return that room
  r=Room(description)
  r.items=bag
  r.name=name
  return r