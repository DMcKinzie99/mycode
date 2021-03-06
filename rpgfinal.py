#!/usr/bin/python3

#DBZ game play
#FINAL PROJECT
# Created by Dalton M. and J H.

from random import randint #use later for final project
#import dice #use for final
#import figlet

def showInstructions():
  #print a main menu and the commands
  print('''
RPG Game of DragonBallZ
=============================
Collect the Dragon Balls &
defeat Majin Buu before you
make your wish at the lookout
==============================
Commands:
  go [ex:north]
  get [item]
  use [item]
  teleport 'tele' [location]
  ''')

def showStatus():
    #print the player's current status
    print('---------------------------')
    print('You are in the ' + currentRoom)
    #print the current inventory
    print('Inventory : ' + str(inventory))
    #Print current health
    print('Your current health is', health)
    #print an item or object if there is one
    if "item" in rooms[currentRoom]:
        print('You see a ' + rooms[currentRoom]['item'])
    if "buu" in rooms[currentRoom]:
        print('You see Majin Buu ready to battle')
    if 'bean' in rooms[currentRoom]:
        print('You see a ' + rooms[currentRoom]['bean'])
    if 'zsword' in rooms[currentRoom]:
        print('You see the  Zsword it might come in handy')
    print("---------------------------")

#starting inventory
inventory = ['Dragon radar']

#starting health
health = 50

#a dictionary linking a room to other rooms
#also shows available items and obbjects
rooms = {

            'Kame house' : {
                  'north' : 'North city',
                  'south' : 'South city',
                  'east'  : 'East city',
                  'west'  : 'West city'
                },
            'North city' : {
                  'north' : 'The lookout',
                  'south' : 'Kame house',
                  'item'  : '1 starball',
                },
            'The lookout' : {
                  'south': 'North city',
                  'item' : '3 starball',
               },
            'East city' : {
                  'north' : 'Tourney grounds',
                  'west' : 'Kame house',
                  'item'  : '7 starball',
               },
            'Tourney grounds' : {
                   'south' : 'East city',
                   'item' : '5 starball',
                   'buu'  : 'Kid buu',
               },
            'South city' : {
                  'south' : 'Satan city',
                  'north' : 'Kame house',
                  'item' : '4 starball',
               },
            'Satan city' : {
                  'north' : 'South city',
                  'item' : '6 starball',
               },
            'West city' : {
                  'east' : 'Kame house',
                  'south' : 'Forest',
                  'item' : '2 starball',
               },
            'Forest' : {
                  'north' : 'West city',
                  'zsword' : 'zsword',
            }
         }

#start at Kame's house
currentRoom = 'Kame house'

showInstructions()

#ball count goes up as you collect dragon balls (7 needed to win)
ball_count = 0

#loop forever until you win
while True:

    showStatus()

    #get the player's next 'move'
    #.split() breaks it up into an list array
    #so typing 'go north' would give the list:
    #['go','east']
    move = ''
    while move == '':
        move = input('>')

    # split allows an items to have a space on them
    move = move.lower().split(" ", 1)

    #if they type 'go' first
    if move[0] == 'go':
        #check that they are allowed wherever they want to go
        if move[1] in rooms[currentRoom]:
            #set the current room to the new room
            currentRoom = rooms[currentRoom][move[1]]
        #trying to make buu attack
            if 'buu' in currentRoom:
                health -= 10
                print('Buu hit you so hard you are nearly dead, hurry and fight back')
                print(health)
            #there is no way to the new rooms then...
        else:
            print('You can\'t go that way!')

    #if they type teleport or tele first
    if move[0] == 'tele' or 'teleport':
        #to teleport they need to have the z sword in inventory
        if move[1] in rooms and 'zsword' in inventory:
            currentRoom = rooms[move[1]]
    #if they type 'get' first
    if move[0] == 'get':
        #if the room contains an item, and the item is the one they want to get
        if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
            #add the item to their inventory
            inventory += [move[1]]
            ball_count += 1
            #display a message of success
            print(move[1] + ' grabbed!')
            print('you currently have', ball_count,'Dragon balls')
            #delete the item from the room
            del rooms[currentRoom]['item']
        elif "ball4" in rooms[currentRoom] and move[1] in rooms[currentRoom]["ball4"]
            print("Seems like a fine day in South City! You are searching around for the Dragon Balls when you see a shady man playing a dice game in the street. You walk up to him and see he has the 4 star Dragon Ball! He claims that he will only give you the Dragon Ball if you can guess the number of the die he is rolling!")
            gamestart = input("Would you care to play a game? (y/n): ")
            if gamestart.lower() == "n":
                break
            elif gamestart.lower() == "y":
                rolldice(1,6)
                dieguess = input("Guess a number between 1 and 6! ")
                    if dieguess == rolldice:
                        print("Hey! You managed to guess right and the shady man gives you the 4 star Dragon Ball")
                        inventory += [move[1]
                        del rooms[currentRoom]["ball4"]

        elif "zsword" in rooms[currentRoom] and move[1] in rooms[currentRoom]['zsword']:
            #add the item to their inventory
            inventory += [move[1]]
            #display a helpful message
            print(move[1] + ' picked up!')
            #delete the item from the room
            del rooms[currentRoom]['zsword']  
        elif 'bean' in rooms[currentRoom] and move[1] in rooms[currentRoom]['bean']:
            #add bean to inventory
            inventory += [move[1]]
            #delete the bean from dict
            del rooms[currentRoom]['bean']
            #display helpful message to mayb use it...
            print(move[1], 'is now in your hand, might be good to use now')
        #otherwise, if the item isn't there to get
        else:
            #tell them they can't get it
            print('Can\'t get ' + move[1] + '!')
 
    if move[0] == 'use':
        #check that they are allowed use this item
        #if move[1] in inventory and rooms[currentRoom]['buu']:
            #random.randint
            #health -= 
        if move[1] in inventory and rooms[currentRoom]['buu']:
            print('The Z Sword was very affective! This is much easier than the series looks.')
            rooms['Kame house']['bean'] = 'senzu bean' #I hope this adds to the dict
            #delete the object from the dict
            del rooms[currentRoom]['buu']
        elif move[1] in inventory:
            health = 50
            del rooms['Kame house']['bean']
            print('You have recovered all of your strength! Let\'s get to the lookout quickly...')
        else:
            print('You don\'t have a weapon strong enough to defeat Buu...')
  
     ## Define how a player can win
    if currentRoom == 'The lookout' and ball_count == 7 and 'buu' not in rooms['Tourney grounds']:
        wish = input('***You summon Shenron***\nShenron roars! TELL ME YOUR WISH... ') #type your wish here
        print("That is out of my power, but I can can give these project makers an A+")
        break
        if currentRoom == 'The lookout' and ball_count == 7 and 'buu' in rooms['Tourney grounds']:
            print("You must defeat Buu before making your wish!")
  

  ## If a player enters a room with a monster
  #elif 'item' in rooms[currentRoom] and 'monster' in rooms[currentRoom]['item']:
   # print('A monster has got you... GAME OVER!')
    #break
