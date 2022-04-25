# character object in an RPG game

class Hero:
    def __init__(self):
       # initalize my characters with the following attributes
       self.hp = 100
       self.dexterity = -4
       self.strength = -6
       self.agility = 20

    def bandage(self):
       self.hp += 25
   
    # edith.attack(akino)
    def attack(self, other_player):
        damage= 100 + self.strength
        other_player.hp -= damage

akino= Hero()
edith= Hero()

print("COMBAT BEGINS!")
print("Akino has the following HP:", akino.hp)
print("Edith winds up and CRACKS Akino!")

edith.attack(akino)

print("Akino now has the following HP:", akino.hp)

akino.bandage()

print("Akino bandages himself, and he now has the following HP:", akino.hp)
