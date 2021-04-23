from adventurelib import *

print("You're falling into a dark, endless hole. You can't see nor hear anything.")
print("It feels like a dream, but you cannot wake up. It's getting warmer and warmer, and suddenly, you stops falling.")
print("You can always type help to see the available command, choose the right things to do and you'll wake up, choose the wrong commands, I'm not sure.")

set_context('dark')
start()

@when("yell", context='dark')
def yell():
  print("You continue falling for about 5 seconds. You stop falling.")
  print("Don't be too loud, you don't know if there's anything near you in the darkness.")

@when("yell", context='light')
def yl():
  print("So you like yelling huh? I see.")

@when("take out the lighter", context='dark')
def lighter():
  set_context('dark')
  set_context('lighter')
  print("You take out the lighter from your pocket.")

@when("light the lighter", context='lighter')
def lit():
  set_context('light')
  print("The darkness disappears as you light up your lighter, why don't you look around?")

#The dice game
@when("pick up the dice")
def dice():
  set_context('dice')
  print("You picked up the 2 dice. They are glowing in your hands.")

@when("roll the dice", context='dice')
def roll():
  number = get_random(2, 12)
  print("You rolled a {number}. Submit or pass?")
  


