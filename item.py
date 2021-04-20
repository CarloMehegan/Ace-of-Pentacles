inv=Bag()

@when("take the ITEM")
@when("take ITEM")
def take(item):
  if current_room.items.take(item):
    inv.add(item)
    print(f"You take the {item}.")
  else:
    print(f"There is no {item} here.")