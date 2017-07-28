#This program is under GNU General Public License v3.0

from random import choice
import sys

def import_species(filename):
    """Importing species from file to dictionary"""
    print("Importing species...",end="")
    
    try:
        file = open(filename,"r")
    except FileNotFoundError:
        print("Failure!\nFile not found! Check if name of file is species_database.txt")
        input("Press any key to exit.")
        sys.exit(1)

    species = {}
    for line in file:
        line = line.rstrip().split(" ")

        if len(line[0]) != 2:
            print("Failure!\nGiven species' shortcut is not 2-char! Correct it in species_database.txt file!") 
            input("Press any key to exit.")
            sys.exit(2)

        if len(line) == 2:
            species[line[0]] = line[1]
        elif len(line) == 3:
            species[line[0]] = line[1] + " " + line[2]
        else:
            print("Failure!\nInvalid file format! Check if each line of species_database.txt "\
                  "contains 2 or 3 strings!")
            input("Press any key to exit.")
            sys.exit(3)
               
    
    file.close()
    print("Done!")
    
    return species

def main():
    """This is where program starts"""

    species_database = import_species("species_database.txt")
    #print(species_database)

    
    print("Thank you for using this software!")
    input("Press any key to exit.")

main()
