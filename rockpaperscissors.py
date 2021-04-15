import random
import colorama
from os import system, name
from colorama import Fore, Style
from time import sleep

aiwin = 0
playerone = 0 
lastcatch = 0

hand = ["rock","paper","scissors"]

def catch(hand, aihand):
    beats = {"rock": "scissors", "paper": "rock", "scissors": "paper"}
    if hand == aihand:
        return "draw"
    if beats[hand] == aihand:
        return ("win")
    else:
        return("loss")

def clear():
    if name == "nt":
        _ = system('cls')

    else:
        _ = system('clear')

while playerone < 3 and aiwin < 3:
    if lastcatch != 0:
        print(lastcatch)
    given = input("Please choose your Hand. 1:Rock 2:Paper 3:Scissors: ")
    given = int(given) -1

    aihand = hand[random.randint(0,2)]
    result = catch(hand[given],aihand)
    if  result == "win":
        lastcatch = "CPU plays {}".format(aihand)+", you play {}.".format(hand[given])+f" {Fore.YELLOW}You win!{Style.RESET_ALL}"
        print(lastcatch)
        playerone +=1
    elif result == "loss":
        lastcatch = "CPU plays {}".format(aihand)+", you play {}.".format(hand[given])+f" {Fore.RED}You lose!{Style.RESET_ALL}"
        print(lastcatch)
        aiwin +=1
    else:
        lastcatch = "Draw!"
        print(lastcatch)
    clear()
if playerone == 3:
    print(lastcatch)
    print("Congratulations, you won a set of 3!")
elif aiwin == 3:
    print(lastcatch)
    print("Sadly, you lost a set of 3!")