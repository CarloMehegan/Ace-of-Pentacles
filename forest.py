from adventurelib import *
import shop

def load(obj):

  set_context("forest")
  @when('look around', context="forest")
  def look():
    print("you see a shop")
    if obj.hp < 10:
      print("You're pretty hurt... You should probably see if they have health potions")

  @when('enter the shop', context="forest")
  def enter():
    shop.load(obj)