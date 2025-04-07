# Import the random library to use for the dice later
import random
import os
import platform

# Put all the functions into another file and import them
import functions
from hero import Hero
from monster import Monster
from crafting import CraftingSystem, Item
from weapon_progression import WeaponProgression

# Print Python version
print(f"Python Version: {platform.python_version()}")

# Print OS name
print(f"Operating System: {os.name}")

# Define two Dice
small_dice_options = list(range(1, 7))
big_dice_options = list(range(1, 21))

# Define the Weapons
weapons = ["Fist", "Knife", "Club", "Gun", "Bomb", "Nuclear Bomb"]

# Define the Loot
loot_options = ["Health Potion", "Poison Potion", "Secret Note", "Leather Boots", "Flimsy Gloves"]
belt = []

# Define the Monster's Powers
monster_powers = {
    "Fire Magic": 2,
    "Freeze Time": 4,
    "Super Hearing": 6
}

# Define the number of stars to award the player
num_stars = 0

# Create Hero, Monster, and WeaponProgression objects
hero = Hero()
monster = Monster()
weapon_system = WeaponProgression()

# Get monsters killed from save file
try:
    with open("save.txt", "r") as file:
        monsters_killed = int(file.readline().strip())
except (FileNotFoundError, ValueError):
    monsters_killed = 0

# Upgrade hero's weapon based on monsters killed
current_weapon = weapon_system.upgrade_hero_weapon(hero, monsters_killed)

# Loop to get valid input for Hero and Monster's Combat Strength
i = 0
input_invalid = True

while input_invalid and i in range(5):
    print("    ------------------------------------------------------------------")
    print("    |", end="    ")
    combat_strength = input("Enter your combat Strength (1-6): ")
    print("    |", end="    ")
    m_combat_strength = input("Enter the monster's combat Strength (1-6): ")

    # Validate input: Check if the string inputted is numeric
    if (not combat_strength.isnumeric()) or (not m_combat_strength.isnumeric()):
        # If one of the inputs are invalid, print error message and halt
        print("    |    One or more invalid inputs. Player needs to enter integer numbers for Combat Strength    |")
        i = i + 1
        continue

    # Note: Now safe to cast combat_strength to integer
    # Validate input: Check if the string inputted
    elif (int(combat_strength) not in range(1, 7)) or (int(m_combat_strength)) not in range(1, 7):
        print("    |    Enter a valid integer between 1 and 6 only")
        i = i + 1
        continue

    else:
        input_invalid = False
        break

if not input_invalid:
    input_invalid = False
    combat_strength = int(combat_strength)
    m_combat_strength = int(m_combat_strength)

    # Roll for weapon
    print("    |", end="    ")
    input("Roll the dice for your weapon (Press enter)")
    ascii_image5 = """
              , %               .           
   *      @./  #         @  &.(         
  @        /@   (      ,    @       # @ 
  @        ..@#% @     @&*#@(         % 
   &   (  @    (   / /   *    @  .   /  
     @ % #         /   .       @ ( @    
                 %   .@*                
               #         .              
             /     # @   *              
                 ,     %                
            @&@           @&@
            """
    print(ascii_image5)
    weapon_roll = random.choice(small_dice_options)

    # Limit the combat strength to 6
    hero.combat_strength = min(6, (combat_strength + weapon_roll))
    print("    |    The hero\'s weapon is " + str(weapons[weapon_roll - 1]))

    # Lab 06 - Question 5b
    functions.adjust_combat_strength(hero.combat_strength, monster.combat_strength)

    # Weapon Roll Analysis
    print("    ------------------------------------------------------------------")
    print("    |", end="    ")
    input("Analyze the Weapon roll (Press enter)")
    print("    |", end="    ")
    if weapon_roll <= 2:
        print("--- You rolled a weak weapon, friend")
    elif weapon_roll <= 4:
        print("--- Your weapon is meh")
    else:
        print("--- Nice weapon, friend!")

    # If the weapon rolled is not a Fist, print out "Thank goodness you didn't roll the Fist..."
    if weapons[weapon_roll - 1] != "Fist":
        print("    |    --- Thank goodness you didn't roll the Fist...")

    # Roll for player health points
    print("    |", end="    ")
    input("Roll the dice for your health points (Press enter)")
    health_points = random.choice(big_dice_options)
    print("    |    Player rolled " + str(health_points) + " health points")

    # Roll for monster health points
    print("    |", end="    ")
    input("Roll the dice for the monster's health points (Press enter)")
    m_health_points = random.choice(big_dice_options)
    print("    |    Player rolled " + str(m_health_points) + " health points for the monster")

    # Collect Loot
    print("    ------------------------------------------------------------------")
    print("    |    !!You find a loot bag!! You look inside to find 2 items:")
    print("    |", end="    ")
    input("Roll for first item (enter)")

    # Collect Loot First time
    loot_options, belt = functions.collect_loot(loot_options, belt)
    print("    ------------------------------------------------------------------")
    print("    |", end="    ")
    input("Roll for second item (Press enter)")

    # Collect Loot Second time
    loot_options, belt = functions.collect_loot(loot_options, belt)

    print("    |    You're super neat, so you organize your belt alphabetically:")
    belt.sort()
    print("    |    Your belt: ", belt)

    # Initialize crafting system
    crafting = CraftingSystem()
    
    # Convert belt items to craftable items
    craftable_inventory = []
    for item_name in belt:
        if "Potion" in item_name:
            craftable_inventory.append(Item(item_name, "potion"))
        elif "Boots" in item_name or "Gloves" in item_name:
            craftable_inventory.append(Item(item_name, "weapon"))
        else:
            craftable_inventory.append(Item(item_name, "herb"))

    # Display craftable items
    print("\n    |    Would you like to craft items? (y/n)")
    if input().lower() == 'y':
        crafting.display_inventory(craftable_inventory)
        
        # Get craftable items
        available_items = crafting.get_craftable_items(craftable_inventory)
        if len(available_items) >= 2:
            print("\n    |    Select two items to combine (enter their numbers):")
            for i, item in enumerate(available_items):
                print(f"    |    {i+1}. {item}")
            
            try:
                choice1 = int(input("    |    First item: ")) - 1
                choice2 = int(input("    |    Second item: ")) - 1
                
                if 0 <= choice1 < len(available_items) and 0 <= choice2 < len(available_items):
                    result = crafting.craft_items(available_items[choice1], available_items[choice2])
                    if result:
                        print(f"    |    Successfully crafted: {result}")
                        # Add the crafted item to the belt
                        belt.append(result)
                else:
                    print("    |    Invalid selection!")
            except ValueError:
                print("    |    Please enter valid numbers!")
        else:
            print("    |    Not enough items to craft!")

    # Use Loot
    belt, hero.health_points = functions.use_loot(belt, health_points)

    print("    ------------------------------------------------------------------")
    print("    |", end="    ")
    input("Analyze the roll (Press enter)")
    # Compare Player vs Monster's strength
    print("    |    --- You are matched in strength: " + str(hero.combat_strength == monster.combat_strength))

    # Check the Player's overall strength and health
    print("    |    --- You have a strong player: " + str((hero.combat_strength + hero.health_points) >= 15))

    # Roll for the monster's power
    print("    |", end="    ")
    input("Roll for Monster's Magic Power (Press enter)")
    ascii_image4 = """
                @%   @                      
         @     @                        
             &                          
      @      .                          

     @       @                    @     
              @                  @      
      @         @              @  @     
       @            ,@@@@@@@     @      
         @                     @        
            @               @           
                 @@@@@@@                

                                      """
    print(ascii_image4)
    power_roll = random.choice(["Fire Magic", "Freeze Time", "Super Hearing"])

    # Increase the monster's combat strength by its power
    monster.combat_strength += min(6, monster.combat_strength + monster_powers[power_roll])
    print("    |    The monster's combat strength is now " + str(
        monster.combat_strength) + " using the " + power_roll + " magic power")

    # Lab Week 06 - Question 6
    num_dream_lvls = -1 # Initialize the number of dream levels
    while True:
        try:
            print("    |", end="    ")
            num_dream_lvls = int(input("How many dream levels do you want to go down? (Enter a number 0-3)"))
            if 0 <= num_dream_lvls <= 3:
                break
            else:
                print("Number entered must be a whole number between 0-3 inclusive, try again")
        except ValueError:
            print("Number entered must be a whole number between 0-3 inclusive, try again")

    if num_dream_lvls != 0:
        hero.health_points -= 1
        crazy_level = functions.inception_dream(num_dream_lvls)
        hero.combat_strength += crazy_level
        print("combat strength: " + str(hero.combat_strength))
        print("health points: " + str(hero.health_points))

    # Fight Sequence
    # Loop while the monster and the player are alive. Call fight sequence functions
    print("    ------------------------------------------------------------------")
    print("    |    You meet the monster. FIGHT!!")
    while monster.health_points > 0 and hero.health_points > 0:
        # Fight Sequence
        print("    |", end="    ")

        # Lab 5: Question 5:
        input("Roll to see who strikes first (Press Enter)")
        attack_roll = random.choice(small_dice_options)
        if not (attack_roll % 2 == 0):
            print("    |", end="    ")
            input("You strike (Press enter)")
            monster.health_points = hero.hero_attacks(monster)
            if monster.health_points == 0:
                num_stars = 3
            else:
                print("    |", end="    ")
                print("------------------------------------------------------------------")
                input("    |    The monster strikes (Press enter)!!!")
                hero.health_points = monster.monster_attacks(hero)
                if hero.health_points == 0:
                    num_stars = 1
                else:
                    num_stars = 2
        else:
            print("    |", end="    ")
            input("The Monster strikes (Press enter)")
            hero.health_points = monster.monster_attacks(hero)
            if hero.health_points == 0:
                num_stars = 1
            else:
                print("    |", end="    ")
                print("------------------------------------------------------------------")
                input("The hero strikes!! (Press enter)")
                monster.health_points = hero.hero_attacks(monster)
                if monster.health_points == 0:
                    num_stars = 3
                else:
                    num_stars = 2

    if(monster.health_points <= 0):
        winner = "Hero"
        monsters_killed += 1  # Increment monsters killed when hero wins
    else:
        winner = "Monster"

    # Final Score Display
    tries = 0
    input_invalid = True
    while input_invalid and tries in range(5):
        print("    |", end="    ")
        hero_name = input("Enter your hero's name: ")
        if hero_name.strip() == "":
            print("    |    Hero name cannot be empty")
            tries += 1
            continue
        input_invalid = False

    if not input_invalid:
        stars_display = "*" * num_stars
        print("    |    Hero " + hero_name + " gets <" + stars_display + "> stars")

        functions.save_game(winner, hero_name, num_stars)

    # Display final message
    print("    |    Game Over! " + hero_name + " has " + str(num_stars) + " stars!")
    print(f"    |    Monsters Killed: {monsters_killed}")
    print(f"    |    Current Weapon: {current_weapon}")


