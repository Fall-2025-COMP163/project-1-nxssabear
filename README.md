## 🏰 COMP 163 - Project 1: Character Creator & Saving/Loading

Name: Vanessa Gray

Date: 28-Oct-2025

AI Usage: AI assisted in development/debugging and this README file, particularly for save_character() and load_character() functions.

## ✨ Project Overview

The Character Creator is an RPG-inspired system for creating and managing game characters. Users can level up with stats, gold, and equipment. Each class has its own strengths, weaknesses, and signature gear, making every character unique.

## 🛡️ Features
1. Character Creation

Choose a name and class for your character.

Classes include Warrior ⚔️, Mage 🪄, Pirate 🏴‍☠️, Admiral 🎖️, Commodore 🐌, Marine and others.

Each class has distinct stats for strength, magic (or special ability), and health.

Characters automatically receive class-themed equipment as a bonus feature.

2. Dynamic Stats

Stats scale naturally with level progression.

Leveling up recalculates stats, reflecting growth and experience.

Ensures each class has unique and balanced stats.

3. File Management

Save character data to a text file in a structured, readable format.

Load character data from a file to continue gameplay.

Handles invalid filenames and missing directories gracefully.

4. Character Sheet Display

Prints a formatted character sheet in the console.

Tracks stats, gold, and equipment for quick reference.

5. Leveling Up

Level up to automatically increase stats.

Encourages strategic development of each hero.

## 🌟 Creative Touches

Class-themed equipment gives characters personality and style.

Stat distributions are designed to reflect class identity: Pirates are brawny, Mages are magical, Admirals are strategic, etc.

The system is expandable, allowing new classes, items, or stats to be added easily.

## 📝 Notes

All functions return structured outputs for testing and ease of use.

Invalid input or missing files are handled gracefully to prevent program crashes.

The equipment system is a bonus feature, enhancing character uniqueness.

## How to Run
python project1_starter.py
