#This program is under GNU General Public License v3.0
#Made by Krzysztof Kiełczewski, 2017

from random import choice
import sys

SHORTCUT_LENGTH = 2
MAX_COMBOS = 100
TIERS_PER_CHALLENGE = 3

def open_file(filename):
    """Opens file and check if file exists in generator's directory."""
    try:
        file = open(filename,"r")
    except FileNotFoundError:
        print("Failure!\nFile not found! Check if name of file is %s"
              % filename)
        end_program(1)

    return file

def end_program(exit_code = 0):
    """Here program ends both successfully or abnormally."""
    input("Press Enter to exit.")
    sys.exit(exit_code)

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
        for i in range(TIERS_PER_CHALLENGE):
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

def ask_number_of_challenges():
    """Here program asks for number of challenge to generate"""

    print("\n\nHow many challenges you want to generate?")
    print("Enter number from 1 to %d or enter 0 to exit..." % MAX_COMBOS)
    
    while True:
        #Checking for valid input
        try:
            amount = int(input("Your choice: "))
            if amount < 0 or amount > MAX_COMBOS:
                raise ValueError
            else:
                break
        except ValueError:
            print("Invalid value! Try again!")
        
    return amount

def ask_name_of_export_file():
    """Program asks for name of exported file."""

    while True:
        try:
            filename = input("Enter name of txt file for exported challenges: ")
            if (filename == "background_database"
                or filename == "challenge_database"
                or filename == "nocombo_database"
                or filename == "species_database"):
                raise ValueError
            else:
                break
        except ValueError:
            print("You can't override database files! Try another name!")

    filename += ".txt"

    return filename

def generate_challenge(species_db,backgrounds_db,no_combo_db,challenges_db):
    """Here program composes challenge with all required databases."""
    
    chosen_challenge = choice(list(challenges_db.keys()))
    
    if challenges_db[chosen_challenge][2] != [""]:
        for banned_background in challenges_db[chosen_challenge][2]:
            if banned_background in backgrounds_db:
                backgrounds_db.pop(banned_background)

    chosen_background = choice(list(backgrounds_db))

    if challenges_db[chosen_challenge][1] != [""]:
        for banned_species in challenges_db[chosen_challenge][1]:
            if banned_species in species_db:
                species_db.pop(banned_species)

    chosen_species = choice(list(species_db))
    while chosen_species+chosen_background in no_combo_db:
        species_db.pop(chosen_species)
        chosen_species = choice(list(species_db))

    chosen_combo = species_db[chosen_species] + " " + backgrounds_db[chosen_background]

    new_challenge = [chosen_species+chosen_background,chosen_combo,chosen_challenge]
    new_challenge.append(challenges_db[chosen_challenge][0])
    return new_challenge

def export_challenges(file,generated_challenges):
    """Here all elements of generated list are exported to output file."""
    iteration = 0
    
    for challenge in generated_challenges:
        iteration += 1

        output = "[Challenge No.%d]\n\n" % iteration
        output += "%s (%s) - %s\n\n" % (challenge[1],challenge[0],challenge[2])

        for tier in range(TIERS_PER_CHALLENGE):
            output += "* Tier %d: %s\n" % (tier+1, challenge[3][tier])

        output += "\n"

        file.write(output)

    #Creating underline for end of export file
    line = ""
    for i in range(100):
        line += "-"

    file.write(line)

def main():
    """This is where program starts."""

    species_database = import_to_dictionary("species_database.txt")
    backgrounds_database = import_to_dictionary("background_database.txt")
    no_combo_database = import_non_available_combos("nocombo_database.txt")
    challenges_database = import_challenges("challenge_database.txt")

    print("\n--WELCOME TO DCSS CHALLENGE GENERATOR!--")

    number_of_challenges = ask_number_of_challenges()

    if number_of_challenges == 0:
        print("You decided not to generate any challenges.")
        print("Thank you for using this software!")
        end_program(0)

    else:
        output_challenges = []

        for i in range(number_of_challenges):
            generated = generate_challenge(species_database, backgrounds_database,
                                           no_combo_database, challenges_database)
            output_challenges.append(generated)

        output_file = open(ask_name_of_export_file(),"w")
        
        export_challenges(output_file,output_challenges)
        output_file.close()

        print("\nExport ended successfully!")
        print("Thank you for using this software!")
        end_program(0)

main()
