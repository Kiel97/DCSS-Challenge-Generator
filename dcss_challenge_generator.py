#This program is under GNU General Public License v3.0

from random import choice
import sys

def import_to_dictionary(filename):
    """Imports database from file to dictionary"""
    print("Importing %s..." % filename[:-12],end="")
    
    try:
        file = open(filename,"r")
    except FileNotFoundError:
        print("Failure!\nFile not found! Check if name of file is %s" % filename)
        input("Press any key to exit.")
        sys.exit(1)

    dictionary = {}
    iteration = 0
    
    for line in file:
        iteration += 1
        line = line.strip().split(" ", maxsplit=1)

        if len(line[0]) != 2:
            print("Failure!\n%s (line %d) is not 2-char! Correct it in %s file!" % (line[0],iteration,filename)) 
            input("Press any key to exit.")
            sys.exit(2)

        dictionary[line[0]] = line[1]
        
    file.close()
    print("Done!")
    
    return dictionary

def import_non_available_combos(filename):
    """Imports bad combos database from file to list"""
    print("Importing non available combos...",end="")

    try:
        file = open(filename,"r")
    except FileNotFoundError:
        print("Failure!\nFile not found! Check if name of file is %s" % filename)
        input("Press any key to exit.")
        sys.exit(1)

    imp_list = []
    iteration = 0
    
    for line in file:
        iteration += 1
        line = line.strip()

        if len(line) != 4:
            print("Failure!\n%s (line %d) is not 4-char! Correct it in %s file!" % (line,iteration,filename))
            input("Press any key to exit.")
            sys.exit(2)
            
        imp_list.append(line)

    file.close()
    print("Done!")
    return imp_list

def main():
    """This is where program starts"""

    species_database = import_to_dictionary("species_database.txt")
    backgrounds_database = import_to_dictionary("background_database.txt")

    no_combo_database = import_non_available_combos("nocombo_database.txt")

    print(no_combo_database)
    
    print("Thank you for using this software!")
    input("Press any key to exit.")

main()
