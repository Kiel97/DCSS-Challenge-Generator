#This program is under GNU General Public License v3.0

from random import choice
import sys

SHORTCUT_LENGTH = 2

def open_file(filename):
    """Opens file and check if file exists in generator's directory."""
    try:
        file = open(filename,"r")
    except FileNotFoundError:
        print("Failure!\nFile not found! Check if name of file is %s"
              % filename)
        end_program(1)

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
            end_program(2)

        dictionary[line[0]] = line[1]
        
    file.close()
    print("%d...Done!" % iteration)
    
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
            end_program(2)
            
        list.append(line)

    file.close()
    print("%d...Done!" % iteration)
    
    return list

def import_challenges(filename):
    """Imports challenges from file to mixed dictionary with lists"""
    print("Importing challenges...",end="")

    file = open_file(filename)

    dictionary = {}
    iteration = 0

    while True:
        #Importing all challenges line by line
        challenge_name = file.readline()

        if challenge_name[:5] != "Name:":
            break

        iteration += 1
        
        challenge_name = challenge_name[6:].strip()
        
        challenge_tiers = []
        for i in range(3):
            tier = file.readline()

            if tier[:6] != ("Tier%s:" % str(i+1)):
                print("Failure!\nExpected 'Tier%s:' data format in %s, challenge No.%d. Correct it!"
                      % (str(i+1), filename, iteration))
                end_program(2)
            
            tier = tier[6:].strip()
            challenge_tiers.append(tier)


        banned_species = file.readline()
        if banned_species[:11] != "BanSpecies:":
            print("Failure!\nExpected 'BanSpecies:' data format in %s, challenge No.%d. Correct it!"
                      % (filename, iteration))
            end_program(2)
        
        banned_species = banned_species[11:].strip().split(" ")


        banned_backgrounds = file.readline()
        if banned_backgrounds[:15] != "BanBackgrounds:":
            print("Failure!\nExpected 'BanBackgrounds:' data format in %s, challenge No.%d. Correct it!"
                      % (filename, iteration))
            end_program(2)
        banned_backgrounds = banned_backgrounds[15:].strip().split(" ")

        dictionary[challenge_name] = [challenge_tiers,banned_species,
                                      banned_backgrounds]

        #Skip blank line
        file.readline()

    file.close()
    print("%d...Done!" % iteration)
    
    return dictionary

def ask_number_of_challenges(max_combos):
    """Here program asks for number of challenge to generate"""

    print("\n\nHow many challenges you want to generate?")
    print("Enter number from 1 to %d" % max_combos, end=" ")
    amount = int(input("or enter 0 to exit..."))
    
    while amount < 0 or amount > max_combos:
        amount = int(input("Invalid value! Try again..."))
        
    return amount

def end_program(exit_code = 0):
    """Here program ends both successfully or abnormally."""
    input("Press any key to exit.")
    sys.exit(exit_code)

def main():
    """This is where program starts."""

    species_database = import_to_dictionary("species_database.txt")
    backgrounds_database = import_to_dictionary("background_database.txt")
    no_combo_database = import_non_available_combos("nocombo_database.txt")
    challenges_database = import_challenges("challenge_database.txt")

    maximum_combos_amount = len(species_database)*len(backgrounds_database)
    maximum_combos_amount -= len(no_combo_database)

    number_of_challenges = ask_number_of_challenges(maximum_combos_amount)

    if number_of_challenges == 0:
        print("You decided not to generate any challenges.")
        print("Thank you for using this software!")
        end_program(0)

main()
