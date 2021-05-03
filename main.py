from adventurelib import *


@when("look around")
def look_woods():
  print(f"You find yourself in a {get_context()}")

@when("enter the CTX")
def change_context(ctx):
  set_context(ctx) # change context
  print(f"You enter the {ctx}.")

@when("search",  context="woods")
def search_woods():
  print("You find a stick")

@when("search", context="field")
def search_field():
  print("You find a sheep. BAAAA.")

set_context("woods")
start()
