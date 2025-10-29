"""
COMP 163 - Project 1: Character Creator & Saving/Loading
Name: Vanessa Gray
Date: 28-Oct-2025
AI Usage: AI was used to assist in the development/debugging of this code: save_character(), load_character() were the main two functions assisted by AI.
"""
import os # for file path operations

# create character
def create_character(name, character_class):
    """
    Creates a new character dictionary with calculated stats
    Returns: dictionary with keys: name, class, level, strength, magic, health, gold
    """
# create base stats
    character = {"name": name,
                 "class": character_class,
                 "level": 1,
                 "strength": 5,
                 "magic": 15,
                 "health": 80,
                 "gold": 100}

# character equipment based on class
    if character_class == "Warrior":
        equipment = "Sword"
    elif character_class == "Mage":
        equipment = "Staff"
    elif character_class == "Admiral":
        equipment = "Marine Coat"
    elif character_class == "Commodore":
        equipment = "Den Den Mushi"
    elif character_class == "Marine":
        equipment = "Rifle"
    else:
        equipment = "Fists"

    return character

# calculate stats based on class and level
def calculate_stats(character_class, level):
    """
    Calculates base stats based on class and level
    Returns: tuple of (strength, magic, health)
    """
    if character_class == "Warrior":
        strength = 25 + (level * 7)
        magic    = 5 + (level * 2)
        health   = 120 + (level * 13)
    elif character_class == "Mage":
        strength = 8 + (level * 2)
        magic    = 30 + (level * 9)
        health   = 90 + (level * 8)
    elif character_class == "Admiral":
        strength = 15 + (level * 4)
        magic    = 25 + (level * 8)
        health   = 110 + (level * 10)
    elif character_class == "Commodore":
        strength = 18 + (level * 5)
        magic    = 12 + (level * 4)
        health   = 100 + (level * 9)
    elif character_class == "Marine":
        strength = 10 + (level * 3)
        magic    = 15 + (level * 4)
        health   = 95 + (level * 9)
    else:
        strength = 5 + (level * 1)
        magic    = 1 + (level * 1)
        health   = 70 + (level * 5)

    return (strength, magic, health)


# save character to file
def save_character(character, filename):
    """
    Saves character to text file in specific format
    Returns: True if successful, False if error occurred
    """
# validate filename
    if filename == "" or filename is None:
        print("Error: Invalid filename")
        return False 

# check if directory exists
    directory = os.path.dirname(filename)
    if directory and not os.path.exists(directory):
        print("Error: Directory does not exist")
        return False

    # write character data to file
    save_character_file = open(filename, 'w')
    save_character_file.write(f"Character Name: {character.get('name')}\n")
    save_character_file.write(f"Class: {character.get('class')}\n")
    save_character_file.write(f"Level: {character.get('level')}\n")
    save_character_file.write(f"Strength: {character.get('strength')}\n")
    save_character_file.write(f"Magic: {character.get('magic')}\n")
    save_character_file.write(f"Health: {character.get('health')}\n")
    save_character_file.write(f"Gold: {character.get('gold')}\n")
    save_character_file.write(f"Equipment: {character.get('equipment')}\n")
    save_character_file.close()
    return True

# load character from file
def load_character(filename):
    """
    Loads character from text file
    Returns: character dictionary if successful, None if file not found
    """

    if not os.path.exists(filename):
        print("Error: File not found")
        return None
    # check if file exists
    load_character_file = open(filename, 'r') # open file for reading
    lines = load_character_file.readlines()
    
    # read character data from file
    with open(filename, 'r') as load_character_file: # open file for reading
        lines = load_character_file.readlines()

    character = {} # create empty dictionary to hold character data
    for line in lines: # iterate through each line in the file
        key = line.strip().split(": ")
        value = line.strip().split(": ")
        key = key[0] # get the key (before the colon)
        value = value[1] # get the value (after the colon)

# populate character dictionary based on keys
        if key == "Character Name":
            character["name"] = value
        elif key == "Class":
            character["class"] = value
        elif key == "Level":
            character["level"] = int(value)
        elif key == "Strength":
            character["strength"] = int(value)
        elif key == "Magic":
            character["magic"] = int(value)
        elif key == "Health":
            character["health"] = int(value)
        elif key == "Gold":
            character["gold"] = int(value)
        elif key == "Equipment":    
            character["equipment"] = value
    load_character_file.close()
    return character

# display character sheet
def display_character(character):
    """
    Prints formatted character sheet
    Returns: None (prints to console)
    """
# print character sheet
    print("=== CHARACTER SHEET ===")
    print(f"Name: {character.get('name')}")
    print(f"Class: {character.get('class')}")
    print(f"Level: {character.get('level')}")
    print(f"Strength: {character.get('strength')}")
    print(f"Magic: {character.get('magic')}")
    print(f"Health: {character.get('health')}")
    print(f"Gold: {character.get('gold')}") 
    print(f"Equipment: {character.get('equipment')}")    

# level up character
def level_up(character):
    """
    Increases character level and recalculates stats
    Modifies the character dictionary directly
    Returns: None
    """
# increase level by 1
    character["level"] = character["level"] + 1
    new_health = calculate_stats(character["class"], character["level"])[2]
    new_magic = calculate_stats(character["class"], character["level"]) [1]
    new_strength = calculate_stats(character["class"], character["level"])[0]

# update character stats
    character["health"] = new_health
    character["magic"] = new_magic
    character["strength"] = new_strength

    print("You leveled up!")
    return character

# Main program area (optional - for testing your functions)
if __name__ == "__main__":
    print("=== CHARACTER CREATOR ===")
    print("Test your functions here!")

    # Example usage:
    char = create_character("TestHero", "Warrior")
    display_character(char)
    save_character(char, "my_character.txt")
    loaded = load_character("my_character.txt")
    display_character(loaded)
    leveled = level_up(loaded)  
    display_character(leveled)
