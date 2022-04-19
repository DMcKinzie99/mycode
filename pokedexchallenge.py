#!/usr/bin/env python3

pokedex={"Bulbasaur":"Grass/Poison",
         "Squirtle":"Water",
         "Charmander":"Fire"}
pokedex["Pikachu"]= "Electric"
x= ", ".join(pokedex.keys())

print(x)

choice= input("Name a Generation 1 starter Pokemon:\n>")
print( pokedex.get(choice, "We have no record of that pokemon!") )

print(pokedex[choice])

