from adventurelib import set_context, when

def load():
  set_context('shop') # built-in function

  @when("look around", context='shop')
  def look():
    print("You see a dusty shop. An old, hunched figure stands beind the counter.")