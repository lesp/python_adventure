#Adventure Game
#Les Pounder 12th October 2013.
#Gillespies Pub, Topping St, Blackpool

from random import *
import random
import time

def wolf():
    health = randrange(1,50,1)
    action = randrange(1,50,1)
    magic = randrange(1,20,1)
    time.sleep(2)
    print (" ### Wolf Battle Stats ### ")
    print ("Health"),(health)
    print ("Action Points"),(action)
    print ("Magic Points"),(magic)

def orc():
    health = randrange(1,50,1)
    action = randrange(1,50,1)
    magic = randrange(1,20,1)
    time.sleep(2)
    print (" ### Orc Battle Stats ### ")
    print ("Health"),(health)
    print ("Action Points"),(action)
    print ("Magic Points"),(magic)

def troll():
    health = randrange(1,50,1)
    action = randrange(1,50,1)
    magic = randrange(1,20,1)
    time.sleep(2)
    print (" ### Troll Battle Stats ### ")
    print ("Health"),(health)
    print ("Action Points"),(action)
    print ("Magic Points"),(magic)

def elf():
    health = randrange(1,50,1)
    action = randrange(1,50,1)
    magic = randrange(1,20,1)
    time.sleep(2)
    print (" ### Elf Battle Stats ### ")
    print ("Health"),(health)
    print ("Action Points"),(action)
    print ("Magic Points"),(magic)

name = raw_input("Choose your name warrior ")
creature = ['orc','troll','elf','wolf']
battle = random.choice(creature)
print ("Greetings"),(name),("You have been chosen to undertake a great challenge")
HP = randrange(0,200,1)
print ("Your Health Points are "),(HP)
AP = randrange(0,200,1)
print ("Your Action Points are "),(AP)
MP = randrange(0,200,1)
print ("Your Magic Points are "),(MP)
time.sleep(2)
print("The game begins.....")
print("Welcome to the land of nightmares"),(name),(", there have been\n many days of darkness since they left.")

print ("*                                 |>>>                    +        ")
print ("+          *                      |                   *       +")
print ("                    |>>>      _  _|_  _   *     |>>>		   ")
print ("           *        |        |;| |;| |;|        |                 *")
print ("     +          _  _|_  _    \\.    .  /    _  _|_  _       +")
print (" *             |;|_|;|_|;|    \\: +   /    |;|_|;|_|;|")
print ("               \\..      /    ||:+++. |    \\.    .  /           *")
print ("      +         \\.  ,  /     ||:+++  |     \\:  .  /")
print ("                 ||:+  |_   _ ||_ . _ | _   _||:+  |       *")
print ("          *      ||+++.|||_|;|_|;|_|;|_|;|_|;||+++ |          +")
print ("                 ||+++ ||.    .     .      . ||+++.|   *")
print ("+   *            ||: . ||:.     . .   .  ,   ||:   |               *")
print ("         *       ||:   ||:  ,     +       .  ||: , |      +")
print ("  *              ||:   ||:.     +++++      . ||:   |         *")
print ("     +           ||:   ||.     +++++++  .    ||: . |    +")
print ("           +     ||: . ||: ,   +++++++ .  .  ||:   |             +")
print ("                 ||: . ||: ,   +++++++ .  .  ||:   |        *")
print ("                 ||: . ||: ,   +++++++ .  .  ||:   |")

q1 = raw_input("Would you like to know more about the darkness? ")
if q1 == "Yes":
    print ("The darkness came from the east, on the waves and winds. \n The shadows came and destroyed all that stood before them")
elif q1 == "yes":
    print ("The darkness came from the east, on the waves and winds. \n The shadows came and destroyed all that stood before them")
elif q1 == "No":
    print ("We travel to the castle of the High King of the land")
elif q1 == "no":
    print ("We travel to the castle of the High King of the land")
else:
    print ("We travel to the castle of the High King of the land")

print ("You travel into a dark forest, you hear a rustle in the darkness.")
print ("When suddenly  "),(battle),("appears...\n")
if battle == "wolf":
    wolf()
elif battle == "troll":
    troll()
elif battle == "orc":
    orc()
elif battle == "elf":
    elf()
