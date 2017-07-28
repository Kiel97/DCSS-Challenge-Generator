#This program is under GNU General Public License v3.0

from random import choice
import sys

def import_database(filename):
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

def main():
    """This is where program starts"""

    species_database = import_database("species_database.txt")
    backgrounds_database = import_database("background_database.txt")
 
    print("Thank you for using this software!")
    input("Press any key to exit.")

main()
