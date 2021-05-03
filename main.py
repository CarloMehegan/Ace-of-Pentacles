from adventurelib import * 
from random import randint
number = 0
life = 2

print("You're falling into a dark, endless hole. You can't see nor hear anything. It feels like a dream, bt you cannot wake up. It's getting warmer and warmer, and suddenly, your back hits against the floor and you stop falling.")
print("In this stage, you'll need to explore this dark place and overcome any challenges that come up to you. Once you have defeated all the enemies, they will give you a hint for your last rolling dice game, which provides an important piece of information to solve the final puzzle.")
print("You can always type help to see the available commands. Choose the right things to do and you'll wake up; choose the wrong commands? I'm not sure.")

#Explore the place
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
  print("You are surrounded by treasure chests. There are # of them.")

#Combat stuff

#The dice game
@when("pick up the dice", context='light')
def dice():
  set_context('dice')
  print("You picked up the 2 dice. They are glowing in your hands.")

@when("roll the dice", context='dice')
def roll():
  global number
  number = randint(2, 12)
  print(f"You rolled a {number}. Submit or pass?")
  set_context('submit or pass')

@when("submit", context='submit or pass')
def submit():
  global number
  global life
  if number == 7:
    print("Correct! On a regular die, add up two opposite sides, and you always get 7. That's why the hint was 'Opposite sides make up perfection.'")
  else:
    print(f"Too bad, {number} is not the correct answer. You now have {life} attempts left.")
    life = life -1
    if life < 0:
      print("Game over. The correct answer is 7. On a regular die, add up two opposite sides, and you always get 7. That's why the hint was 'Opposite sides make up perfection.'")
      print("Unfortunately, you'll have to continue your journey without the important piece of information to solve the final puzzle from this room. Good luck!")
      set_context('game over')
    else:
      set_context('dice') 

@when("pass", context='submit or pass')
def again():
  print("You passed. That was a safe decision. You can roll the dice again to find the correct answer.")
  set_context('dice')

set_context('dark')
start()
  


