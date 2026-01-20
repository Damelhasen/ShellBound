
""" Authors : Johan Sheby , Chriss John Francis , Ayham Al-Dibeh
    Date : 11-01-2026
 A simple Adventure game in terminal"""
# chriss 2:10PM
import random
import time
import os
from colorama import Fore, Style
import winsound

# Variables

Player_Name = "John"
Player_Class = 0
player_hp = 0
Attack_Modifier = 0
Player_AC = 0
Dexterity = 0
Classes = {"Ranger","Fighter","Wizard"}



def play_sound(file):
    winsound.PlaySound(file, winsound.SND_FILENAME)
play_sound("WHISTLE.wav")
def death():
    # save inventory to txt file
    with open("Savefile.txt", "w") as file:
        for item in inventory:
            file.write(f"{item['name']},{item['quantity']}\n")

    typewriter(f"""Game Over. Your adventure ends here... \n \
                       ______
        .-"      "-.
       /            \
      |              |
      |,  .-.  .-.  ,|
      | )(__/  \__)( |
      |/     /\     \|
      (_     ^^     _)
       \__|IIIIII|__/
        | \IIIIII/ |
        \          /
         `--------` \n
    {Player_Name} the {Player_Class} has fallen in the Whispering Woods.
                       """)

    exit()

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
        time.sleep(0.01)
    print()

def Player_Attack(attcker_name:str, attack_modifier:int, defender_ac:int, damage_roll:int):

    attacK_roll = roll_dice(20,attack_modifier) 
    if attacK_roll >= defender_ac : 
        player_hp = player_hp - damage_roll
        print(f"{attcker_name} hits {player_hp} for {damage_roll} damage!")
    elif attacK_roll >= 20 : 
        player_hp = player_hp - (damage_roll *2)
        print(f"{attcker_name} lands a CRITICAL HIT on {player_hp} for {damage_roll *2} damage!")
    else : 
        print(f"{attcker_name} misses {player_hp}!")

def player_defend(attcker_name:str, attack_modifier:int, defender_ac:int, damage_roll:int, player_hp:int) :
    attacK_roll = roll_dice(20,attack_modifier) 
    if attacK_roll >= defender_ac : 
    
        player_hp = player_hp - damage_roll
        print(f"{attcker_name} hits {Player_Name} for {damage_roll} damage!")
    else : 
        print(f"{attcker_name} misses {Player_Name}!")
    
    return player_hp

inventory = [
    {"name": "Wool  Shirt", "quantity": 1},
    {"name": "Leather Pants", "quantity": 1},
    {"name": "Gold Coins", "quantity": 5},
]

def display_inventory():
    #show inventory
    print("\nINVENTORY:")
    for item in inventory:
        print(f"  - {item['name']} x{item['quantity']}")
    print()

def add_item(name, quantity):
    #adds new stuff but icrease
    for item in inventory:
        if item["name"] == name:
            item["quantity"] += quantity
            return
    inventory.append({"name": name, "quantity": quantity})

def display_enemy(enemy_name, enemy_health):
    """Display ASCII enemy"""
    if enemy_name == "Goblin":
        print(f"""
    {Fore.GREEN}___
   /o o\\
   \\ o /
    |O|{Style.RESET_ALL} {enemy_name} (HP: {enemy_health})
   /| |\\
    | |
   /   \\
        """)
    elif enemy_name == "Orc":
        print(f"""
    {Fore.RED} /\\_/\\
    ( o.o ){Style.RESET_ALL} {enemy_name} (HP: {enemy_health})
     > ^ <
    /|   |\\
      | |
        """)
    elif enemy_name == "Bandit":
        print(f"""
    {Fore.RED} 
     {enemy_name} (HP: {enemy_health})
     ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣶⣤⣀⣀⣤⣶⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⣿⣿⣿⣿⣿⣿⣿⣿⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠆⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⣾⣷⣶⣶⣶⣦⣤⠀⢤⣤⣈⣉⠙⠛⠛⠋⣉⣁⣤⡤⠀⣤⣴⣶⣶⣶⣾⣷⠀
⠀⠈⠻⢿⣿⣿⣿⣿⣶⣤⣄⣉⣉⣉⣛⣛⣉⣉⣉⣠⣤⣶⣿⣿⣿⣿⡿⠟⠁⠀
⠀⠀⠀⠀⠀⠉⠙⠛⠛⠿⠿⠿⢿⣿⣿⣿⣿⡿⠿⠿⠿⠛⠛⠋⠉⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢿⣷⠦⠄⢀⣠⡀⠠⣄⡀⠠⠴⣾⡿⠀⠀⠀⠀⠀⣀⡀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢤⣤⣴⣾⣿⣿⣷⣤⣙⣿⣷⣦⣤⡤⠀⠴⠶⠟⠛⠉⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠏⠀⠺⣷⣄⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢈⣙⣛⣻⣿⣿⣿⡿⠃⠐⠿⠿⣾⣿⣷⡄⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⣿⣿⣿⠿⠋⠀⠀⠀⠀⠀⠀⠀⠈⠁⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣿⣿⣿⣾⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠛⠛⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
        """)

def combat(player_name, player_hp, player_attack, player_ac,
           enemy_name, enemy_hp, enemy_attack, enemy_ac):

    print(f"\n{Fore.RED}=== COMBAT START ==={Style.RESET_ALL}")
    time.sleep(1)

    while player_hp > 0 and enemy_hp > 0:
        clear_screen()
        display_enemy(enemy_name, enemy_hp)
        print(f"\n{player_name} HP: {player_hp}")

        choice = input("\n1. Attack\n2. Defend\n3. Run\nChoose: ").strip()

        # player turn
        if choice == "1":
            roll = roll_dice(20, player_attack)
            if roll == 20:
                damage = roll_dice(6, 0) * 2
                enemy_hp -= damage
                print(f"{Fore.GREEN}CRITICAL HIT! You deal {damage} damage!{Style.RESET_ALL}")
            elif roll >= enemy_ac:
                damage = roll_dice(6, 0)
                enemy_hp -= damage
                print(f"You hit the {enemy_name} for {damage} damage!")
            else:
                print("You miss!")

        elif choice == "2":
            print("You brace for the enemy’s attack.")
            player_ac += 2  # temporary boost

        elif choice == "3":
            print("You try to run away...")
            if roll_dice(20, 0) >= 12:
                print("You escape successfully!")
                return False, player_hp
            else:
                print("You fail to escape!")

        else:
            print("Invalid choice!")
            continue

        time.sleep(1)

        # enemy turn
        if enemy_hp > 0:
            roll = roll_dice(20, enemy_attack)
            if roll >= player_ac:
                damage = roll_dice(6, 0)
                player_hp -= damage
                print(f"The {enemy_name} hits you for {damage} damage!")
            else:
                print(f"The {enemy_name} misses!")

        # reset defend bonus
        if choice == "2":
            player_ac -= 2

        input("\nPress Enter to continue...")

    # combat result
    if player_hp > 0:
        print(f"{Fore.CYAN}You defeated the {enemy_name}!{Style.RESET_ALL}")
        return True, player_hp
    else:
        print(f"{Fore.RED}You have been defeated...{Style.RESET_ALL}")
        return False, player_hp
        
        ######Variables#####
Player_Name = "John"
Player_Class = 0
player_hp = 0
Attack_Modifier = 0
Player_AC = 0
Dexterity = 0
Classes = {"Ranger","Fighter","Wizard"}


def main():
    intro()
    input("Press Enter to start your adventure...")
    clear_screen()

    # ----- CHARACTER CREATION -----
    Player_Name = input("Enter your character's name: ")
    clear_screen()

    while True:
        Player_Class = input(
            "Choose your class:\n"
            "1. Ranger\n"
            "2. Fighter\n"
            "3. Wizard\n"
            "Enter the number of your choice: ")

        if Player_Class == "1":
            player_hp = 10
            Attack_Modifier = 2
            Player_AC = 14
            Dexterity = 3
            Player_Class = "Ranger"
            break
        elif Player_Class == "2":
            player_hp = 12
            Attack_Modifier = 3
            Player_AC = 16
            Dexterity = 2
            Player_Class = "Fighter"
            break
        elif Player_Class == "3":
            player_hp = 8
            Attack_Modifier = 4
            Player_AC = 12
            Dexterity = 1
            Player_Class = "Wizard"
            break
        else:
            print("Invalid choice.")

    clear_screen()
    print(f"Welcome, {Player_Name} the {Player_Class}!")
    print(f"HP: {player_hp} | ATK: {Attack_Modifier} | AC: {Player_AC}")
    input("\nPress Enter to continue...")
    clear_screen()

    # ----- INTRO STORY -----
    typewriter(
        "You awaken in the Whispering Woods. Rain falls softly as an old man sits by a campfire.\n"
        "A strange scroll lies near your hand..."
    )

    has_scroll = False

    # ----- CAMP LOOP -----
    while True:
        choice = input(
            "\nWhat do you do?\n"
            "1. Ask about the scroll\n"
            "2. Ask where you are\n"
            "3. Leave the camp\n"
        )

        # ----- SCROLL -----
        if choice == "1":
            typewriter("The old man eyes the scroll carefully. 'Powerful magic,' he mutters.")
            keep = input("Do you keep the scroll? (Y/N): ").upper()

            if keep == "Y" and not has_scroll:
                add_item("Fireball Spell Scroll", 1)
                has_scroll = True
                typewriter("You place the scroll into your pack.")
            else:
                typewriter("You decide to leave it for now.")

        # ----- LOCATION -----
        elif choice == "2":
            typewriter(
                "'You are in the Whispering Woods,' the old man says.\n"
                "'Few who enter find their way out unscathed.'"
            )

        # ----- LEAVE CAMP -----
        elif choice == "3":
            typewriter("You step away from the fire and into the dark woods...")
            play_sound("Monster.wav")
            break

        else:
            print("Invalid choice.")

    clear_screen()

    # ----- FIRST COMBAT -----
    enemy = random.choice(["Goblin", "Orc"])
    enemy_hp = 15 if enemy == "Goblin" else 20
    enemy_attack = 1 if enemy == "Goblin" else 2
    enemy_ac = 12 if enemy == "Goblin" else 13

    victory, player_hp = combat(
        Player_Name,
        player_hp,
        Attack_Modifier,
        Player_AC,
        enemy,
        enemy_hp,
        enemy_attack,
        enemy_ac
    )

    if not victory:
        death()

    # ----- LOOT + MAP -----
    add_item("Gold Coins", random.randint(5, 15))
    add_item("Map", 1)

    typewriter("Searching the body, you find gold and a strange map.")

    look = input("Examine the map? (Y/N): ").upper()
    if look == "Y":
        typewriter("The map marks a place called the Ancient Ruins.")

        go = input("Travel to the Ancient Ruins? (Y/N): ").upper()
        if go == "Y":
            typewriter("You follow the map deeper into the forest...")
            play_sound("SNAP.wav")

            # ----- BANDIT FIGHT -----
            victory, player_hp = combat(
                Player_Name,
                player_hp,
                Attack_Modifier,
                Player_AC,
                "Bandit",
                18,
                2,
                14
            )

            if not victory:
                death()

            typewriter("The bandit falls. The ruins await beyond...")

    # ----- END CHECK -----
    typewriter("You take a moment to check your belongings.")
    display_inventory()
    typewriter("To be continued...")


if __name__ == "__main__":   
    main()