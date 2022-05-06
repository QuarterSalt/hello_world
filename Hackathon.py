# Coding Notes:

# Averages for the stats:
#       -> heal points = 100, physical power = 30, dexterity = 30, stamina = 30, light magic = (dependant on race), dark magic = (dependant on race)

# Averages for equipment:
#       -> armour = 30, weapon = 30





# Race stats
Human = {"hp":80,"phy_pow":15,"dex":30,"sta":30,"light_magic":35,"dark_magic":0,}
Human_equip = {"armour=light":20,"weapon=broadsword":30}



# User setup
    # Name

while True:
    user_name = input("What is your name?: ")
    if user_name != "":
        break


        # Race
user_race = input("Welcome "+user_name+", chose your race: Human, Demon, Dragonkin, Elf, Dwarf, Halfling, Vampire or Giant: ")
while True:
    if user_race != "Human" or "Demon" or "Dragonkin" or "Elf" or "Dwarf" or "Halfing" or "Vampire" or "Giant":
        break


user_race_stats = input("Would you like to know your Race's stats? Y/N?: ")
while True:
    if user_race_stats == "Y" or "y":
        print(user_race)


# Game intro
print("\n\nHello "+user_name+"\nWelcome to The Maze Game\n\n\nThe Maze Game is a Game all about completing levels 1 by 1.\n")
print("Firstly, I the great one, creator of this maze, will be sending one of my minions to test your skill.\n")
print("")
action_1 = input("")