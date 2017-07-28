#This program is under GNU General Public License v3.0

from random import choice
import sys

SHORTCUT_LENGTH = 2

def open_file(filename):
    """Opens file and check if file exists in generator's directory."""
    try:
        file = open(filename,"r")
    except FileNotFoundError:
        print("Failure!\nFile not found! Check if name of file is %s" % filename)
        input("Press any key to exit.")
        sys.exit(1)

    return file


def import_to_dictionary(filename):
    """Imports database from file to dictionary."""
    print("Importing %s..." % filename[:-13],end="")
    
    file = open_file(filename)

    dictionary = {}
    iteration = 0
    
    for line in file:
        iteration += 1
        line = line.strip().split(" ", maxsplit=1)

        if len(line[0]) != SHORTCUT_LENGTH:
            print("Failure!\n%s (line %d) is not %d-char! Correct it in %s file!"
                  % (line[0],iteration,SHORTCUT_LENGTH,filename)) 
            input("Press any key to exit.")
            sys.exit(2)

        dictionary[line[0]] = line[1]
        
    file.close()
    print("Done!")
    
    return dictionary

def import_non_available_combos(filename):
    """Imports bad combos database from file to list."""
    print("Importing non available combos...",end="")

    file = open_file(filename)

    list = []
    iteration = 0
    
    for line in file:
        iteration += 1
        line = line.strip()

        if len(line) != SHORTCUT_LENGTH*2:
            print("Failure!\n%s (line %d) is not %d-char! Correct it in %s file!"
                  % (line,iteration,SHORTCUT_LENGTH*2,filename))
            input("Press any key to exit.")
            sys.exit(2)
            
        list.append(line)

    file.close()
    print("Done!")
    return list

def main():
    """This is where program starts."""

    species_database = import_to_dictionary("species_database.txt")
    backgrounds_database = import_to_dictionary("background_database.txt")

    no_combo_database = import_non_available_combos("nocombo_database.txt")
    
    print("Thank you for using this software!")
    input("Press any key to exit.")

main()
