
""" Author : Johan Sheby 
    Date : 11-01-2026
 A simple Adventure game in terminal"""

import random
import time
import os
from colorama import Fore, Style

Player_Name = ""
Player_Class = 0
Player_Health = 0
Attack_Modifier = 0
Player_AC = 0
Dexterity = 0

Classes = {"Ranger","Fighter","Wizard"}
def intro()  :
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

def Player_Attack(attcker_name:str, attack_modifier:int, defender_ac:int, damage_roll:int) :
    attacK_roll = roll_dice(20,attack_modifier) 
    if attacK_roll >= defender_ac : 
        Player_Health = Player_Health - damage_roll
        print(f"{attcker_name} hits {Player_Health} for {damage_roll} damage!")
    elif attacK_roll >= 20 : 
        Player_Health = Player_Health - (damage_roll *2)
        print(f"{attcker_name} lands a CRITICAL HIT on {Player_Health} for {damage_roll *2} damage!")
    else : 
        print(f"{attcker_name} misses {Player_Health}!")

def player_defend(attcker_name:str, attack_modifier:int, defender_ac:int, damage_roll:int) :
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

if __name__ == "__main__":   
    main()