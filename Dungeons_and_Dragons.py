
""" Author : Johan Sheby 
    Date : 11-01-2026
 A simple Adventure game in terminal"""

import random
import time
import os
from colorama import Fore, Style

Player_Name = "john"
Player_Class = 0
Player_Health = 0
Attack_Modifier = 0
Player_AC = 0
Dexterity = 0

Classes = {"Ranger","Fighter","Wizard"}
def intro():
    ART = ("""                                                     
                                                        
                        ..=##=..                      
                    ..++:.-=.:++..                   
                    ..*+..   -=  ...=#..                
            ...:#=.....:=#@@#=:.....-#:...           
            .=*:.:=+*=:. .*::*. .:=*+=:.:*=..         
        .+%#+=-....    .=:...+.   .....-=+#%*..      
        .#..            +..  ..+             .#..     
        .#+.           *:      .#            =#..     
        .++..        .*:        .#.        ..*+..     
        .+:+.       .+.          .*.       .=:+.      
        .+.*:      .+..           .*.      .#.+..     
        .+ .+.    .#.              .#.    .=. +..     
        .*  +:   .#.                .%.   .*. +..     
        .*  .*. .*..                ..*. .+.  +..     
        .*  .=: *.                    .*..=.  +..     
        .+   .%#....                   .##.   +..     
        .+  .**%-:::::::::::::::::::::::%+#.  =:.     
        :*#-.   -*..                ..+-   .-#*:.     
        .:*=...  .==..             .-+.  ...=*:..     
            .=*:   .+-.           :*.   :+=.          
            ...-#-...#.        .%:..-#-...           
                    ..#+.:*      *-.=#..                
                    ..+*+=..=*+*..                   
                        ..=##=..                      
                                                        
                                                        """)
    print(ART)
    print("""""
  ____  _          _ _ ____                        _ 
 / ___|| |__   ___| | | __ )  ___  _   _ _ __   __| |
 \___ \| '_ \ / _ \ | |  _ \ / _ \| | | | '_ \ / _` |
  ___) | | | |  __/ | | |_) | (_) | |_| | | | | (_| |
 |____/|_| |_|\___|_|_|____/ \___/ \__,_|_| |_|\__,_|
                                                     
""""")
def clear_screen():
    cmd = 'cls' if os.name == 'nt' else 'clear'
    try:
        res = os.system(cmd)
        if res != 0:
            print("\n" * 100)
    except Exception:
        print("\n" * 100)

def roll_dice(sides:int,modifier:int) :
    return random.randint(1,sides) + modifier 

def typewriter(text):
    for char in text:
        print(char, end='')
        time.sleep(0.05)
    print()

def Player_Attack(attcker_name:str, attack_modifier:int, defender_ac:int, damage_roll:int):
    attacK_roll = roll_dice(20,attack_modifier) 
    if attacK_roll >= defender_ac : 
        Player_Health = Player_Health - damage_roll
        print(f"{attcker_name} hits {Player_Health} for {damage_roll} damage!")
    elif attacK_roll >= 20 : 
        Player_Health = Player_Health - (damage_roll *2)
        print(f"{attcker_name} lands a CRITICAL HIT on {Player_Health} for {damage_roll *2} damage!")
    else : 
        print(f"{attcker_name} misses {Player_Health}!")

def player_defend(attcker_name:str, attack_modifier:int, defender_ac:int, damage_roll:int):
    attacK_roll = roll_dice(20,attack_modifier) 
    if attacK_roll >= defender_ac : 
    
        Player_Health = Player_Health - damage_roll
        print(f"{attcker_name} hits {Player_Name} for {damage_roll} damage!")
    else : 
        print(f"{attcker_name} misses {Player_Name}!")

def main() : 
    intro()
    input("Press Enter to start your adventure...")
    clear_screen()
    
    Player_Name = input("Enter your character's name: ")
    clear_screen()
    while True:
        Player_Class = input(f"Enter your character's class \n"
            f"{Fore.GREEN}1. Ranger{Style.RESET_ALL}\n"
            f"{Fore.RED}2. Fighter{Style.RESET_ALL}\n"
            f"{Fore.BLUE}3. Wizard{Style.RESET_ALL}\n")
        if Player_Class not in {"1", "2", "3"}:
            print("Invalid class. Please choose from:\n" 
            f"{Fore.GREEN}1. Ranger{Style.RESET_ALL} \n" \
            f"{Fore.RED}2. Fighter{Style.RESET_ALL} \n" \
            f"{Fore.MAGENTA}3. Wizard{Style.RESET_ALL}")
            continue
        if Player_Class == "1":
            Player_Health = 10
            Attack_Modifier = 2
            Player_AC = 14
            Dexterity = 3
            Player_Class = "Ranger"
        elif Player_Class == "2":
            Player_Health = 12
            Attack_Modifier = 3
            Player_AC = 16
            Dexterity = 2
            Player_Class = "Fighter"
        elif Player_Class == "3":
            Player_Health = 12
            Attack_Modifier = 3
            Player_AC = 16
            Dexterity = 2
            Player_Class = "Wizard"
        break
    
    print(f"Welcome, {Player_Name} the {Player_Class}!")
    print(f"Health: {Player_Health}, Attack Modifier: {Attack_Modifier}, Armor Class: {Player_AC}, Dexterity: {Dexterity}")
    clear_screen()
    typewriter("""The rain is the first thing you feel—cold, relentless, and smelling of ancient pine.

You are lying on a bed of damp ferns in the heart of the Whispering Woods. Above, the canopy is so thick that the midday sun is reduced to mere threads of grey light. Your head throbs with the rhythm of a war drum, and your memories are shrouded in a thick, magical fog. The last thing you remember was a flash of violet light and the sound of breaking glass.

"Careful there," a voice calls out.

Through the mist, an old traveler sits by a small, sputtering campfire a few yards away. He is sharpening a rusted dagger, the metallic shing-shing echoing through the trees.

"The goblins usually pick these woods clean by sundown," the old man says without looking up. "You’re lucky I found you first. You’ve got the look of someone who’s traveled far, though your gear has seen better days."

He finally turns to look at you, his eyes milky with age but sharp with curiosity. He gestures to a tattered scroll lying near your hand.

"That parchment there... it has a seal I haven't seen in fifty years. I can't read the script, but I assume it belongs to you.""")
    choice_1 = input("""What Would you like to do? \n
    1. Ask the old man about the scroll. \n
    2. Inquire about your current location and situation. \n
    3.Leave for the woods \n""")

if __name__ == "__main__":   
    main()