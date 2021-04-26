from adventurelib import * 
from random import randint

print("You're falling into a dark, endless hole. You can't see nor hear anything.")
print("It feels like a dream, but you cannot wake up. It's getting warmer and warmer, and suddenly, you stops falling.")
print("You can always type help to see the available commands. Choose the right things to do and you'll wake up; choose the wrong commands? I'm not sure.")

@when("yell", context='dark')
def yell():
  print("That was not a great thing to do. Don't be too loud when you don't know if there's anything near you in the darkness.")

@when("yell", context='light')
def yl():
  print("So you like yelling huh? I see.")

@when("take out the lighter", context='dark')
def lighter():
  set_context('lighter')
  print("You take out the lighter from your pocket.")

@when("light the lighter", context='lighter')
def lit():
  set_context('light')
  print("The darkness disappears as you light up your lighter, why don't you look around?")

@when("look around", context='light')
def look():
  print("You are surrounded by Poker cards and dice.")

#The dice game
@when("pick up the dice", context='light')
def dice():
  set_context('dice')
  print("You picked up the 2 dice. They are glowing in your hands.")

@when("roll the dice", context='dice')
def roll():
  number = randint(2, 12)
  print(f"You rolled a {number}. Submit or pass?")

set_context('dark')
start()
  


