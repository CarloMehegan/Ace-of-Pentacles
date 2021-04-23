from adventurelib import *


def get_look_command(name, description):
  bag = "stuff"
  @when(f'look around the {name}')
  def look():
    print(f"{description}")
    print(bag)

  return look