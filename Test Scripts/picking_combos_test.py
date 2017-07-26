#This script is a piece of logic responsible for choosing combos from species
#and background, rolling again if chosen combo is bad and then adding
#full name to output message

#Importing choice function which pick one element from list
from random import choice

#Species and backgrounds 2-char database
species = ["Hu","DE","Fo"]
backgrounds = ["Fi","Wz","AK","FE"]

#Description of imported species and backgrounds
species_description = {"Hu":"Human", "DE":"Deep Elf", "Fo":"Formicid"}
backgrounds_description = {"Fi":"Fighter", "Wz":"Wizard", "AK":"Abyssal Knight",
                        "FE":"Fire Elementalist"}

#List of impossible to choose combos or ones with very low attidute
bad_combos = ["DEFi", "DEAK", "FoFE"]

def pickCombo():
    species_chosen = choice(species)
    
    while True:
        #This loop picks random combo and checks if it is bad one
        background_chosen = choice(backgrounds)

        output = species_chosen + background_chosen

        if output not in bad_combos:
            break
        
    output += ": " + species_description[species_chosen]+" "+\
    backgrounds_description[background_chosen]

    return output

print(pickCombo())
