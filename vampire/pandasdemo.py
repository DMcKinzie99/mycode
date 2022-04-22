#!/usr/bin/env python3

import pandas as pd

import random as ran

pokedf= pd.read_csv("pokedex.txt", index_col=1)

#Get rid of dupes

pokedf.drop_duplicates(inplace=True)

print(pokedf)

#Sort pokemon alphabetically

sorteddf= pokedf.sort_values(["Legendary", "Name"])

print(sorteddf)


