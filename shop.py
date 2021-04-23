from adventurelib import set_context, when
import forest

def load(obj):

  set_context('shop') # built-in function

  @when("look around", context='shop')
  def look():
    print("You see a dusty shop. An old, hunched figure stands beind the counter.")

  @when("introduce myself")
  def intro():
    if obj.hp < 10:
      print("You don't look so good... Here's a health potion")
      obj.hp = 100
    else:
      print("You introduce yourself")
      print(f"The person says: 'Hello, {obj}!'")

  @when("leave")
  def leave():
    print("You enter the forest")
    forest.load(obj)

  # i could add more...