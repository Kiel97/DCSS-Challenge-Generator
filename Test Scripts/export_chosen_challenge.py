def importChallengeDatabase(filepath):
    print("Importing challenge database...",end="")
    database = []
    database_file = open(filepath,'r')

    for line in database_file:
        if "Name: " in line:
            fetched_line = line[6:].rstrip()
            database += [[fetched_line]]

        elif "Tier1: " in line or "Tier2: " in line or "Tier3: " in line:
            fetched_line = line[7:].rstrip()
            database[-1].append(fetched_line)

        elif "BanSpecies: " in line:
            fetched_line = line[12:].rstrip()
            database[-1] += [fetched_line.split(" ")]

        elif "BanBackgrounds: " in line:
            fetched_line = line[16:].rstrip()
            database[-1] += [fetched_line.split(" ")]
    
    database_file.close()
    print("Done!\n\n")
    return database

def main():
    challenge_database = importChallengeDatabase("C:/Users/User/Documents/Python Files/DCSS Challenge Generator/challenges_database.txt")
    for element in challenge_database:
        print(element)

main()
