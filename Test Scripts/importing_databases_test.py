def import_from_txt_to_dict(filepath):
    print("Importing...",end="")
    dictionary = {}
    database_file = open(filepath,'r')

    for line in database_file:
        line = line.rstrip().split(" ")

        if len(line) == 2:
            dictionary[line[0]] = line[1]
        else:
            dictionary[line[0]] = line[1] + " " + line[2]
        
    
    database_file.close()
    print("Done!")
    return dictionary

def import_from_txt_to_list(filepath):
    print("Importing...",end="")
    import_list = []

    database_file = open(filepath,'r')

    for line in database_file:
        line_split = line.rstrip().split("\n")

        import_list += line_split
    
    print("Done!")
    return import_list

species = import_from_txt_to_dict("C:/Users/User/Documents/Python Files/DCSS Challenge Generator/species_database.txt")
backgrounds = import_from_txt_to_dict("C:/Users/User/Documents/Python Files/DCSS Challenge Generator/background_database.txt")
bad_combos = import_from_txt_to_list("C:/Users/User/Documents/Python Files/DCSS Challenge Generator/badcombo_database.txt")

print("\n\nImported stuff:")
print(species)
print(backgrounds)
print(bad_combos)
