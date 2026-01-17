
""" Author : Johan Sheby 
    Date : 11-01-2026
 A simple Adventure game in terminal"""

import random
import time
import os
from colorama import Fore, Style



Player_Name = "john"
Player_Class = 0
player_hp = 0
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

def player_defend(attcker_name:str, attack_modifier:int, defender_ac:int, damage_roll:int) :
    global player_hp
    attacK_roll = roll_dice(20,attack_modifier) 
    if attacK_roll >= defender_ac : 
    
        player_hp = player_hp - damage_roll
        print(f"{attcker_name} hits {Player_Name} for {damage_roll} damage!")
    else : 
        print(f"{attcker_name} misses {Player_Name}!")


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

def combat(player_name, player_hp, player_attack, player_ac, enemy_name, enemy_hp, enemy_attack, enemy_ac):
    
    
    player_hp = player_hp
    
    print(f"\n{Fore.RED}=== COMBAT START ==={Style.RESET_ALL}")
    
    while player_hp > 0 and enemy_hp > 0:
        display_enemy(enemy_name, enemy_hp)
        print(f"{player_name} HP: {player_hp}\n")
        
        action = input("1. Attack  2. Defend\n Run away \n Choose: ").strip()
        
        if action == "1":
            # Player 
            attack_roll = roll_dice(20, player_attack)
            if attack_roll >= enemy_ac:
                damage = roll_dice(6, 0)
                enemy_hp -= damage
                print(f"{Fore.CYAN}[Roll: {attack_roll}] You hit for {damage} damage!{Style.RESET_ALL}")
            else:
                print(f"{Fore.YELLOW}[Roll: {attack_roll}] You miss!{Style.RESET_ALL}")
        elif action == "2":
            print(f"{Fore.BLUE}You brace for impact...{Style.RESET_ALL}")
        
        clear_screen()
        
        # Enemy attacks 
        if enemy_hp > 0:
            player_defend(enemy_name, enemy_attack, player_ac, roll_dice(6, 0))
        
        input("Press Enter to continue...")
        clear_screen()
    
    if player_hp > 0:
        print(f"{Fore.GREEN}Victory! You defeated the {enemy_name}!{Style.RESET_ALL}")
        return True
    else:
        print(f"{Fore.RED}You have been defeated...{Style.RESET_ALL}")
        return False

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
            player_hp = 10
            Attack_Modifier = 2
            Player_AC = 14
            Dexterity = 3
            Player_Class = "Ranger"
        elif Player_Class == "2":
            player_hp = 12
            Attack_Modifier = 3
            Player_AC = 16
            Dexterity = 2
            Player_Class = "Fighter"
        elif Player_Class == "3":
            player_hp = 12
            Attack_Modifier = 3
            Player_AC = 16
            Dexterity = 2
            Player_Class = "Wizard"
        break

    
    print(f"Welcome, {Player_Name} the {Player_Class}!")
    print(f"Health: {player_hp}, Attack Modifier: {Attack_Modifier}, Armor Class: {Player_AC}, Dexterity: {Dexterity}")
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
    if int(choice_1) != 1 or int(choice_1) != 2 or int(choice_1) != 3 :
        print("Invalid choice. Please select 1, 2, or 3.")
    if int(choice_1) == 1 :
        typewriter(f"""You pick up the scroll, its edges frayed and the seal cracked. "This looks important," you say, as you read it you realize its a Fire ball spell scroll """)
        scroll_choice = input(typewriter(f"""Would Like to keep it ? Y/N"""))
        if scroll_choice.upper() == "Y" : 
            typewriter("You carefully tuck the scroll into your pack, feeling a strange warmth emanating from it.")
            inventory.append({"name": "Fireball Spell Scroll", "quantity": 1})
        elif scroll_choice.upper() == "N" : 
            typewriter("You decide to leave the scroll behind, unsure of its significance.")
    elif int(choice_1) == 2 :
        typewriter(f"""You look around, taking in the dense foliage and the towering trees. "Where am I?" you ask the old man. He sighs, "You're in the Whispering Woods, a place of both wonder and danger. As for how you got here, I can't say. But you look like you've been through quite an ordeal." """)
    elif int(choice_1) == 3 :
        typewriter("You decide to leave the safety of the campfire and venture into the woods.")
        clear_screen()
        typewriter("As you walk deeper into the forest, you hear a growl...")
        clear_screen()
        
        # Random enemy encounter
        import random
        enemy = random.choice(["Goblin", "Orc"])
        enemy_hp = 15 if enemy == "Goblin" else 20
        enemy_attack = 1 if enemy == "Goblin" else 2
        enemy_ac = 12 if enemy == "Goblin" else 13
        
        typewriter(f"A wild {enemy} appears!")
        clear_screen()
        
        victory = combat(Player_Name, player_hp, Attack_Modifier, Player_AC, enemy, enemy_hp, enemy_attack, enemy_ac)
        
        if victory:
            add_item("Gold Coins", random.randint(10, 25))
            typewriter("You loot the creature and find some gold!")
        else:
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
  jgs    `--------` \n
    {Player_Name} the {Player_Class} has fallen in the Whispering Woods.
                       """)
            return

if __name__ == "__main__":   
    main()