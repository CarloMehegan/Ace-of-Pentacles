from adventurelib import *
  @when('north', direction = 'north')
  @when('south', direction = 'south')
  @when('east', direction = 'east')
  @when('west', direction = 'west'):

  def go(direction):
    global current_room
    room = current_room.exit(direction)
    if room:
      current_room = room
      print(f"you go {dirrection}.")
      look()
start()