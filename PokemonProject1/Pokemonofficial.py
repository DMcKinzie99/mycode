#!/usr/bin/env python3

#This will be a script that decides what Pokemon the user is!

Bulbasaur={"Type":"Grass", "Color":"Green", "Size":"Small", "Toes": "3"}
Squirtle={"Type":"Water", "Color":"Blue", "Size":"Small", "Toes":"3"}
Charmander={"Type":"Fire", "Color":"Orange", "Size":"Small","Toes":"4"}
Chikorita={"Type":"Grass", "Color":"Light Green", "Size":"Small", "Toes":"1"}
Totodile={"Type":"Water", "Color":"Blue/Red", "Size":"Small", "Toes":"5"}
Cyndaquil={"Type":"Fire", "Color":"Dark Blue", "Size":"Small", "Toes":"1"}
#^^^My Database of Pokemon
counter=1
print(type(Bulbasaur))

Type=input("What type of Pokemon do you you think you are? Fire, Water, Or Grass? ")#This would be the start of collecting info. from the user.

if Type == "Grass":
    Color=input("What color do you feel describes you more? Green or Green?")
    if Color=="Green":
        Toes=input("How many toes do you think a Pokemon should have? 1 or 3?")
        if Toes >= "3":
            print("Wow! You seem to be a Bulbasaur!")
            while counter <5:
                print("MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM")
                counter += 1
        elif Toes < "3":
            print("Looks like you are a Chikorita, Congratulations!")
            while counter <5:
                print("MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM")
                counter += 1
if Type == "Fire":
    Color=input("What Color do you feel describes you more? Red or Dark Blue?")
    if Color=="Red":
        print("Looking like a Charmander today")
        while counter <5:
            print("Fwoosh Fwoosh Fwoosh!")
            counter += 1
    elif Color=="Dark Blue":
        print("You are a Cyndaquil!")
        while counter <5:
            print("Fwoosh Fwoosh Fwoosh!")
            counter += 1

if Type == "Water":
    Color =input("Would you choose the color Blue or Blue?")
    if Color== "Blue":
        Toes=input("How many toes do you like on your blue pokemon?")
        if Toes>="5":
            print("Wow you would be a Totodile! ")
            while counter <5:
                print("Splash Splash Splash!")
                counter += 1
        elif Toes < "5":
            print("You are a Squirtle! ")
            while counter < 5:
                print("Splash Splash Splash!")
                counter += 1
        
