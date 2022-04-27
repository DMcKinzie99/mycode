#!/usr/bin/python3

from random import randint
import dice
import sys
import os



def showInstructions():
  #print a main menu and the commands
  print('''
The object of the game it to collect the items and go from room to room. 
========
Commands:
  go [north, south, east, west, up, down]
  get [item]
  use [item]
  inv/inventory
  Type 'help' at anytime! Type 'q'to quit!
''')

def showStatus():
  #print the player's current status
  print('---------------------------')
  print('You are in the ' + currentRoom)
  #print the current inventory
  print('Inventory : ' + str(inventory))
  #print an item if there is one
  if "item" in rooms[currentRoom]:
    print('You see a ' + rooms[currentRoom]['item'])
  print("---------------------------")

#an inventory, which is initially empty
inventory = []

#a dictionary linking a room to other rooms
## A dictionary linking a room to other rooms
rooms = {

            'Hall' : {
                  'south' : 'Kitchen',
                  'east'  : 'Dining Room',
                  'west'  : 'East Forrest',
                  'item'  : 'key',
                  'item'  : 'shield of reflection',
                  'item_status' : ' hinding within the mirrors',
                  'desc'  : 'You are in the hall of mirrors. What you see may not be and what you be may not see. Move quickly.',
                },

            'Kitchen' : {
                  'north' : 'Hall',
                  'item'  : 'fork',
                  'item' : 'spoon',
                  'desc' : 'You are in the kitchen. Sit down and have a meal',
                },
            'Dining Room' : {
                  'west'  : 'Hall',
                  'south' : 'Garden',
                  'item'  : 'potion',
                  'north' : 'Pantry',
                  'desc' : 'You are in the dining room. Have some whine.',
               },
            'Garden' : {
                  'north' : 'Dining Room'
               },
            'Bathroom' : {
                  'west' : 'Dining Room',
                  'east' : 'Battle Room',
                  'item' : 'blinding towel',
                  'item' : 'deathly gas',
                  'desc' : 'You are in the bathroom. Get the towel and the gas',
                  },
            'Battle Room' : {
                  'west'  : 'Bathroom'
                  'south' : 'North Forrest',
                  'north' : 'South Forrest',
                  'east'  : 'West Forrest',
                  'desc'  : 'You are in the Battle Room. Get out quick or face the monster.'
                  },
            'East Forrest': {

            'Pantry' : {
                  'south' : 'Dining Room',
                  'item'  : 'cookie',
                  'desc' : 'You are in the pantry. Take a break and relax before going on.',
            }
         }

#start the player in the Hall
currentRoom = 'Hall'

showInstructions()

#loop forever
while True:

  showStatus()

  #get the player's next 'move'
  #.split() breaks it up into an list array
  #eg typing 'go east' would give the list:
  #['go','east']
  move = ''
  while move == '':
    move = input('>')

  # split allows an items to have a space on them
  # get golden key is returned ["get", "golden key"]          
  move = move.lower().split(" ", 1)

  #if they type 'go' first
  if move[0] == 'go':
    #check that they are allowed wherever they want to go
    if move[1] in rooms[currentRoom]:
      #set the current room to the new room
      currentRoom = rooms[currentRoom][move[1]]
    #there is no door (link) to the new room
    else:
        print('You can\'t go that way!')

  #if they type 'get' first
  if move[0] == 'get' :
    #if the room contains an item, and the item is the one they want to get
    if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
      #add the item to their inventory
      inventory += [move[1]]
      #display a helpful message
      print(move[1] + ' got!')
      #delete the item from the room
      del rooms[currentRoom]['item']
    #otherwise, if the item isn't there to get
    else:
      #tell them they can't get it
      print('Can\'t get ' + move[1] + '!')
      
  ## Define how a player can win
  if currentRoom == 'Garden' and 'key' in inventory and 'potion' in inventory:
    print('You escaped the house with the ultra rare key and magic potion... YOU WIN!')
    break

    elif move[0] == 'help':
        showInstructions()

    elif move[0] in ['q', 'quit]']:
        print("Are you sure you want to quit? Yes/No")
        quit_query = input('>')
        if quit_query.lower() in ['y', 'yes']:
            print("Thanks for playing!")
            sys.exit()
  ## If a player enters a room with a monster
  elif 'item' in rooms[currentRoom] and 'monster' in rooms[currentRoom]['item']:
    print('A monster has got you... GAME OVER!')
    break 
