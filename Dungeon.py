import random
from tabnanny import check
from turtle import numinput
line = "----------------------------------------"

def percentage(num):
    p30 = 30/100
    resutles = float(num) * p30
    return resutles

class PlayerClass():

    health: int = 100
    lifePotions = 0
    shieldState = False
    shieldUsedTimes = 0

    def GetPlayerName(self, input: str):
        self.Name = input.title()

    def Profile(self):
        print("\n\nPlayers Profile:")
        print(f"Health:   {self.health}")
        print(f"Potions:   {self.lifePotions}")
        if self.shieldState == True :
            print("Shield:   True")
            print(f"-- You got {6 - self.shieldUsedTimes} turns before your shield break.")
        else :
            print("Shield:   False")
        print("\n\n")

    def Attacking(self):
        attacks = [13, 14, 15, 25]
        rand = random.choice(attacks)
        return rand

    def Damage(self, attack):
        if self.shieldUsedTimes > 5 :
            self.shieldState = False
            self.shieldUsedTimes = 0

        if self.shieldState == True :
            self.health -= int(round(percentage(attack)))
            self.shieldUsedTimes += 1
            print(f"{self.Name} got damaged {round(percentage(attack))} health points, for luck s/he had a shield.\nYour current Health is: {self.health}/100 .")
        else :
            print(attack)
            self.health -= attack
            print(f"{self.Name} got damaged {attack} health points.\nYour current Health is: {self.health}/100 .")

    def Healing(self):
        if self.health <= 80 and self.lifePotions != 0 :
            self.health += 20
            self.lifePotions -= 1
            print(f"Your current health is: {self.health}")

        elif self.health > 80 and self.lifePotions != 0 :
            self.health = 100
            self.lifePotions -= 1
            print(f"Your current health is: {self.health}")
        else :
            print(f"{self.Name} is out of life potions!")

    def GotShield(self):
        self.shieldState = True
        self.shieldUsedTimes = 0

class MonsterClass():
    health = 40
    attacks = [10, 12, 14]
    def Attacking(self) -> int :
        rand = random.choice(self.attacks)
        return rand

class DragonClass():
    health = 100

    def Attacking(self):
        attacks = [12, 15, 19, 20]
        rand = random.choice(attacks)
        return rand

    def Damage(self, att):
        self.health -= int(att)

player = PlayerClass()

player.GetPlayerName(str(input("Enter your player's name here: ")))

print(f"Hi! {player.Name}, after a long journy of exploring and learning new experiences...\n You found the CURSED DUNGEON.")
print(line)
playerAnswer = str(input("Do you want to go to the inside?\n1- Yes\n2- No\n").lower())

if playerAnswer == "y" or "yes" or "1" :
    print(f"{player.Name} Entered the dungeon.")
elif playerAnswer == "n" or "no" or "2" :
    print(f"{player.Name} didn't feel comfortable, so he tried to stay away from the dungeon but...\nEvil spirits pulled him inside.\n{player.Name} Now is in the dungeon.")
else :
    print(f"Welp, somehow {player.Name} teleported inside the dungeon")
print(line)

monster1 = MonsterClass()
print(f"{player.Name} found a monster!\nThe monster attacked {player.Name} !\n");player.Damage(monster1.Attacking())
print("You drew your sword and killed the monster, and fortunately he dropped 2 lifePotions.\nYou drank one of them.")
player.lifePotions += 2
player.Healing()

print("While you ware walking inside the dungeon, You found an old warrior trader.\nHe said 'You are the chosen one' and he keept saying it over and over while he was lying on the ground.\nSuddenly... he stands up and give you 3 lifepotions and a shield, then he disappeared!")
player.lifePotions += 3; player.GotShield()

print(f"{player.Name} starts walking though a SPECIAL road in the dungeon, a- what???\nit feels numzy and dizy... woWwowOOw\n{player.Name} found him/her self infront a SPECIAL GATE\n{player.Name} decided to go in !")
print(f"({player.Name}): It's dark here.\n(???): Yes it is. *sudden boss music plays in the background*\nYUP, It's time to fight a boss\n[A dragon apears from the darkness]")
boss = DragonClass()
print("You both start fighting !")

Win = False

def checkHealing():
    if player.lifePotions > 0 :
        print("3- Heal (20 health points)")
        return True
    else : 
        return False


while Win == False :

    print(f'The Dragon attacked {player.Name}!\n'); player.Damage(boss.Attacking())
    if player.health <= 0 :
        print(f"{player.Name} has died, LOL\nBetter next time...")
        break
    print(f"It's {player.Name}'s turn")
    while True :
        Act = None
        print("chose one of the followings choices:")
        print("1- Show player states")
        print("2- Attack")
        checkH = checkHealing()
        ans = input("Your choice: ")
        if ans == "1" :
            player.Profile(); continue
        elif ans == "2" :
            att = player.Attacking() ; boss.Damage(att);Act = 2; break
        elif ans == "3" and checkH == True :
            player.Healing(); break
        else :
            print("MAKE A CHOICE !\nTry using the numbers of the choices."); continue
    if Act == 2 :
        print(f"{player.Name} attacked the dragon and delt {att} damage points")
    if boss.health <= 0 :
        Win = True; break
    print(f"{player.Name} health:   {player.health}\nDragon health:   {boss.health}\nIt's the boss1 turn now!")
if Win == True :
    print(f"\n\n{player.Name} Won! and s/he escaped the dungeon alive")
    player.Profile()








