from adventurelib import *
@when("awake", context='puzzle')
def wake():
  print("you awaken in strange a room.")

@when("look", context='puzzle')
def seeing():
  print("You look at your surroundings.")

@when("letter", context='puzzle')
def letter():
  print(" the first thing you see is a letter .")

@when("read", context='puzzle')
def read():
  print(" the letter states in order to leave the room you need to solve a riddle.")

@when("hint", context='puzzle')
def hints():
  print("it is an object that most people use after dinner .")


@when("riddle", context='puzzle')
def riddle():
  print(" I am full of holes but I still hold water.")



@when("the answer is ANSWER", context='puzzle')
def solve(answer):
  if answer == 'sponge':
    print("A door opens you have answerd correctly .")
  else:
    print("that answer is wrong")
  
@when("walk", context='puzzle')
def walk():
  print(" you walk to the open door it leads to an other room.")

@when("keys", context='puzzle')
def keys ():
  print(" you see three keys one is made of gold the second silver the third tungsten..")

@when("door", context='puzzle')
def door():
  print(" there are 3 doors for three keys the locks on the doors have numbers on them they represent melting points find the correct melting point for the three keys.")

@when(" melting", context='puzzle')
def melting():
 print(" the first door is 1,763°f the second is 1,948°f the third is 6,192°f .")

gold_door = Item("the second door")
gold_door.locked = True

silver_door = Item("the first door")
silver_door.locked = True 

tungsten_door = Item("the third door")
tungsten_door.locked = True


@when("try the KEY key in the DOOR door")
def try_door(key, door):
  if key == "gold" and door == "second":
    print("You are successful!")
    gold_door.locked = False
  elif key == "silver" and door == "first":
   silver_door.locked = False 
   print ("you are successful!")
  elif key == "tungsten"and door == "third":
     print ("you are successful!")
     tungsten_door.locked = False
  else:
    print(f"The {key} key doens't fit in the {door} door")

  if not gold_door.locked and not silver_door.locked and not tungsten_door.locked:
    print("All the door merge into a portal you have successfully escaped congrats")