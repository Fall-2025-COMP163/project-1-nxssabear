"""
COMP 163 - Project 1: Character Creator & Saving/Loading
Name: Vanessa Gray
Date: 28-Oct-2025
AI Usage: AI was used to assist in the development/debugging & README of this code: save_character(), load_character() were the main two functions assisted by AI.
"""
import os

def create_character(name, character_class):
    """
    Creates a new character dictionary with calculated stats
    Returns: dictionary with keys: name, class, level, strength, magic, health, gold
    """

    character = {"name": name,
                 "class": character_class,
                 "level": 1,
                 "strength": 5,
                 "magic": 15,
                 "health": 80,
                 "gold": 100}
    
    if character_class == "Warrior":
        equipment = "Sword"
    elif character_class == "Mage":
        equipment = "Staff"
    elif character_class == "Rogue":
        equipment = "Dagger"
    elif character_class == "Cleric":
        equipment = "Book"
    else:
        equipment = "Fists"

    return character

def calculate_stats(character_class, level):
    """
    Calculates base stats based on class and level
    Returns: tuple of (strength, magic, health)
    """

    if character_class == "Warrior":
        strength    = 20 + (level * 7)
        magic       = 1 + (level * 1)
        health      = 100 + (level * 15)
    elif character_class == "Mage":
        strength    = 10 + (level * 1)
        magic       = 15 + (level * 8)
        health      = 95 + (level * 10)
    elif character_class == "Rogue":
        strength    = 15 + (level * 2)
        magic       = 7 + (level * 3)
        health      = 80 + (level * 7)
    elif character_class == "Cleric":
        strength    = 8 + (level * 2)
        magic       = 10 + (level * 4)
        health      = 85 + (level * 5)
    else:
        None
    
    return (strength, magic, health)

def save_character(character, filename):
    """
    Saves character to text file in specific format
    Returns: True if successful, False if error occurred
    """

    if filename == "" or filename is None:
        print("Error: Invalid filename")
        return False 
    
    directory = os.path.dirname(filename)
    if directory and not os.path.exists(directory):
        print("Error: Directory does not exist")
        return False
    
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

def load_character(filename):
    """
    Loads character from text file
    Returns: character dictionary if successful, None if file not found
    """
    load_character_file = open(filename, 'r')
    lines = load_character_file.readlines()

    character = {}
    for line in lines:
        key = line.strip().split(": ")
        value = line.strip().split(": ")
        key = key[0]
        value = value[1]

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

def display_character(character):
    """
    Prints formatted character sheet
    Returns: None (prints to console)
    
    Example output:
    === CHARACTER SHEET ===
    Name: Aria
    Class: Mage
    Level: 1
    Strength: 5
    Magic: 15
    Health: 80
    Gold: 100
    """
    # TODO: Implement this function
    pass

def level_up(character):
    """
    Increases character level and recalculates stats
    Modifies the character dictionary directly
    Returns: None
    """
    # TODO: Implement this function
    # Remember to recalculate stats for the new level
    pass

# Main program area (optional - for testing your functions)
if __name__ == "__main__":
    print("=== CHARACTER CREATOR ===")
    print("Test your functions here!")
    
    # Example usage:
    # char = create_character("TestHero", "Warrior")
    # display_character(char)
    # save_character(char, "my_character.txt")
    # loaded = load_character("my_character.txt")
