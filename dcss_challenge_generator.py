#This program is under GNU General Public License v3.0

from random import choice
import sys

def import_species(filename):
    """Imports species from file to dictionary"""
    print("Importing species...",end="")
    
    try:
        file = open(filename,"r")
    except FileNotFoundError:
        print("Failure!\nFile not found! Check if name of file is species_database.txt")
        input("Press any key to exit.")
        sys.exit(1)

    species = {}
    for line in file:
        line = line.strip().split(" ", maxsplit=1)

        if len(line[0]) != 2:
            print("Failure!\nGiven species' shortcut is not 2-char! Correct it in species_database.txt file!") 
            input("Press any key to exit.")
            sys.exit(2)

        species[line[0]] = line[1]               
    
    file.close()
    print("Done!")
    
    return species

def import_backgrounds(filename):
    """Imports backgrounds from file to dictionary"""
    backgrounds = {}
    return backgrounds

def main():
    """This is where program starts"""

    species_database = import_species("species_database.txt")
    backgrounds_database = import_backgrounds("background_database.txt")

    
    print("Thank you for using this software!")
    input("Press any key to exit.")

main()
