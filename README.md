# DCSS Challenge Generator

## Introduction
Have you ever had a moment when you were looking on forum for new Casual League Challenge but nobody posts new one?
Have you ever been bored with playing different combos and had no side objectives which would make game more exciting?
Or are you looking for new combinations to play you never thought about?

Then this brand new DCSS Challenge Generator is for you! Inspired by The Tavern's various challenges (mainly by triorph's Casual League Weeks) I have written Python script which from different species, background and challenge
databases combines new Tavern's style challenges. Here are some advantages of this program:

- Provide database files in script's directory, enter number of challenges to generate and output file name! Ready!
- Generate your challenges ready to share with others. No need to spend time on cleaning up output file.
- Too easy or too hard challenges? Or too few of them? Or maybe you are playing one of DCSS forks? Customise your databases
  with user-editing friendly .txt format! Create your own challenges!
- Hate limit of generating up to 100 challenges or your species and background shortcuts are not 2-char length?
  Or maybe you want to add new feature to program? Thanks to Python it's very easy to edit and add your own lines code even for 
  programming beginners! Grab your repository clone and use your imagination!
  
What are you waiting for? Challenge yourself in Dungeon Crawl Stone Soup! :+1:



## Requirements for program to work

This script requires 4 files that MUST name exactly:
- **species_database.txt** - contains all species to choose from
- **background_database.txt** - contains all backgrounds to choose from
- **nocombo_database.txt** - contains all impossible to start game combos
- **challenge_database.txt** - contains all basic challenges to choose from

Program also requires Python (preferably 3.6.0 or higher) to work, Python doesn't compile script to executable file but 
interprets it every time program is launched.

## File format of input files

This program uses external databases in straight way, so files MUST be in specific format to import them correctly.
If you want to include more tiers per challenge, you need to edit TIERS_PER_CHALLENGE constant in program's code and then
edit challenge file.
Here are file templates:

### species_database.txt:
Structure:
```
(species 2-char shortcut)(species fullname - may be longer than 2 words)
```

Example:
```
S1 Species Name1
S2 Species Name 2
...
Gh Ghoul
```

### background_database.txt:
Structure:
```
(background 2-char shortcut)(background fullname - may be longer than 2 words)
```

Example:
```
B1 Background Name1
B2 Background Name 2
...
VM Venom Mage
```

### nocombo_database.txt:

Structure:
```
(species 2-char shortcut)(background 2-char shortcut)
```

Example:
```
BnCm
BnCm
...
MuTm
```

### challenge_database.txt

Structure of:
```
Name: (Challenge name)
Tier1: (Description of tier 1)
Tier2: (Description of tier 2)
Tier3: (Description of tier 3)
BanSpecies: (All species shortcuts to ban from choosing in this challenge, leave empty if all permitted)
BanBackgrounds: (All background shortcuts to ban from choosing in this challenge, leave empty if all permitted)
(Empty line!! - For less cluttered file so user has easier time to analyze challenges included in file)
```
Example:
```
Name: Challenge for beginners
Tier1: Reach lair
Tier2: Get rune
Tier3: Win game
BanSpecies: VS Vp Dg Fo Na Op Fe Ba Mu Gn
BanBackgrounds:

Name: Challenge for hardcores
Tier1: Reach last floor of Lair before reaching experience level 9
Tier2: Acquire all 5 pandemonic runes as a first 5 runes
Tier3: Win game with all 15 runes before reaching experience level 20
BanSpecies:
BanBackgrounds: Fi Gl Mo Hu As Ar Wn Be AK CK Sk Tm Wr AM En Wz Cj Ne FE IE AE EE VM
...
```

### Contribution

If you want to add more exciting challenges, report misspell or even add new functionalities to source code,
don't hesistate to contribute. The more patches, the better program will be. Just download copy of repository and
adjust it your way!

### Future Goals
- [ ] MOOOOOORE CHALLENGESSSS
- [ ] Convert console program to GUI program
- [ ] Species with god combos instead of backgrounds
- [ ] Challenges with gods to choose and ban
