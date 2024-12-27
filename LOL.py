import sqlite3

connection = sqlite3.connect("LOL.db")
print(connection.total_changes)  
cursor = connection.cursor()

with open('initDatabase.sql', 'r') as datainit:
    sqlFile = datainit.read()

commands = sqlFile.strip().split(';')
championCount = 0
for command in commands:
    if command.strip():  
        cursor.execute(command.strip() + ';')
connection.commit()

#add functions!!
def addChampion(name, abilities, relDate, difficulty):
    cursor.execute(
        "INSERT INTO Champions (champion_name, abilities, date_released, difficulty) VALUES (?, ?, ?, ?)",
        (name, abilities, relDate, difficulty)
    )
    connection.commit()
    print(name, "has been added!")

def addChampionLore(champion_name, lore_name, region):
    cursor.execute(
        "INSERT INTO Champion_Lore (champion_name, lore_name, region) VALUES (?, ?, ?)",
        (champion_name, lore_name, region)
    )
    connection.commit()
    print(champion_name, "linked with lore", lore_name, "in region", region,"!")

def addSkinLine(skin_series):
    cursor.execute(
        "INSERT INTO Skin_Lines (skin_series) VALUES (?)",
        (skin_series,)
    )
    connection.commit()
    print(skin_series, "has been added!")

def addChampionSkin(champion_name, skin_series, skin_name):
    cursor.execute(
        "INSERT INTO Champion_Skins (champion_name, skin_series, skin_name) VALUES (?, ?, ?)",
        (champion_name, skin_series, skin_name)
    )
    connection.commit()
    print("Skin", skin_name, "for", champion_name, "in skin series", skin_series,"has been added!")

def addItem(item_name, health, attack_damage, attack_speed, armor, magic_resist, movement_speed):
    cursor.execute(
        "INSERT INTO Items (item_name, health, attack_damage, attack_speed, armor, magic_resist, movement_speed) VALUES (?, ?, ?, ?, ?, ?, ?)",
        (item_name, health, attack_damage, attack_speed, armor, magic_resist, movement_speed)
    )
    connection.commit()
    print(item_name, "has been added!")

def addChampionItem(champion_name, item_name, common_item, damage_type):
    cursor.execute(
        "INSERT INTO Champion_Items (champion_name, item_name, common_item, damage_type) VALUES (?, ?, ?, ?)",
        (champion_name, item_name, common_item, damage_type)
    )
    connection.commit()
    print("Item", item_name,"has been linked to",champion_name,"with damage type",damage_type,"!")


#function to add lots of data into the database!
def fillDB():   
    addChampion("Ahri", "Orb of Deception, Fox-Fire, Charm, Spirit Rush", "2011-10-04", "Intermediate")
    addChampion("Yasuo", "Steel Tempest, Wind Wall, Sweeping Blade, Last Breath", "2013-12-13", "Hard")
    addChampion("Lux", "Light Binding, Prismatic Barrier, Lucent Singularity, Final Spark", "2010-06-23", "Easy")
    addChampion("Ezreal", "Mystic Shot, Essence Flux, Arcane Shift, Trueshot Barrage", "2010-02-16", "Medium")

    #i put madeup names cause i think riot games is changing all the stories recently
    addChampionLore("Ahri", "Fox Demon", "Ionia")
    addChampionLore("Yasuo", "Unforgiven", "Ionia")
    addChampionLore("Lux", "Love", "Demacia")
    addChampionLore("Ezreal", "Love", "Piltover")

    addSkinLine("Project")
    addSkinLine("Star Guardian")
    addSkinLine("Arcade")
    addSkinLine("Victorious")

    addChampionSkin("Ahri", "Project", "Project Ahri")
    addChampionSkin("Yasuo", "Winterblessed", "Winterblessed Yasuo")
    addChampionSkin("Lux", "Star Guardian", "Star Guardian Lux")
    addChampionSkin("Ezreal", "Battle Bunny", "Battle Bunny Ezreal")

    addItem("Infinity Edge", 0, 70, 0, 0, 0, 0)
    addItem("Boots of Speed", 0, 0, 0.25, 0, 0, 0)
    addItem("Rabadon's Deathcap", 0, 120, 0, 0, 0, 0)
    addItem("Guardian Angel", 0, 40, 0, 0, 0, 0)

    addChampionItem("Ahri", "Rabadon's Deathcap", "Common", "Magic")
    addChampionItem("Yasuo", "Infinity Edge", "Common", "Physical")
    addChampionItem("Lux", "Rabadon's Deathcap", "Common", "Magic")
    addChampionItem("Ezreal", "Guardian Angel", "Common", "Physical")


#Demonstrates a primary important use-case query
def showAllChampions():
    champions = cursor.execute("SELECT * FROM Champions").fetchall()
    for champion in champions:
        print(f"Champion: {champion[0]}, Abilities: {champion[1]}, Release Date: {champion[2]}, Difficulty: {champion[3]}")
#Demonstrates a second important use-case query
def showAllItems():
    items = cursor.execute("SELECT * FROM Items").fetchall()
    for item in items:
        print(f"Item: {item[0]}, Health: {item[1]}, Attack Damage: {item[2]}, Attack Speed: {item[3]}, Armor: {item[4]}, Magic Resist: {item[5]}, Movement Speed: {item[6]}")

#Both functions below are queries that involve an N:N relationship 
def searchForChampionByLoreName(lore_name):
    champions = cursor.execute("SELECT champion_name FROM Champion_Lore WHERE lore_name = ?", (lore_name,)).fetchall()
    if champions:
        for champion in champions:
            print(f"Champion associated with Lore[{lore_name}]: {champion[0]}")
    else:
        print(f"No champions found with the lore[{lore_name}]")

#This one specifically Demonstrates
# a query that involves a secondary refinement as you must 
# see the champion list before knowing the lore name   
def searchForLoreNameByChampion(champion_name):
    lore_names = cursor.execute("SELECT lore_name FROM Champion_Lore WHERE champion_name = ?", (champion_name,)).fetchall()
    if lore_names:
        for lore in lore_names:
            print(f"Lore associated with {champion_name}: {lore[0]}")
    else:
        print(f"No lore found for champion: {champion_name}")



#User experience!!

#inject Data!
fillDB()

#User Menu!!
while True:
    print("Choose what to do:\n  [1] Show All Champions\n  [2] Show All Items\n  [3] Search For Champion By Lore Name\n  [4] Search For Lore Name By Champion\n  [5] Add New Things\n  [0] Exit")
    inputA = input("Choose an Option: ")
    if (inputA=='1'):
        showAllChampions()
    elif (inputA=='2'):
        showAllItems()
    elif (inputA=='3'):
        inputB = input("What is the lore name? [Capitalize First Letters of Each Word!]\nEnter: ")    
        searchForChampionByLoreName(inputB)
    elif (inputA=='4'):
        inputB = input("What is the Champion name? [Capitalize First Letters of Each Word!]\nEnter: ")
        searchForLoreNameByChampion(inputB)
    elif (inputA == '5'):
        while True:
            inputB = input("Choose an Option\n  [1] Add Champion!\n  [2] Add Lore\n  [0] Exit Add Menu\n Choose: ")  
            if inputB == '1':
                champion_name = input("Enter the champion's name [Capitalize First Letters of Each Word!]: ")
                abilities = input("Enter the champion's abilities [Format(each letter should be an ability): Q,W,E,R]: ")
                rel_date = input("Enter the champion's release date (YYYY-MM-DD): ")
                difficulty = input("Enter the champion's difficulty (Easy, Medium, Hard): ")
                addChampion(champion_name, abilities, rel_date, difficulty)
            elif inputB == '2':
                champion_name = input("Enter the champion's name [Capitalize First Letters of Each Word!]: ")
                lore_name = input("Enter the lore's name [Capitalize First Letters of Each Word!]: ")
                region = input("Enter the region [Capitalize First Letters of Each Word!]: ")
                addChampionLore(champion_name, lore_name, region)
            elif inputB == '0':
                break
            else:
                print("Invalid option. Please choose again.")          
    elif (inputA=='0'):
            break
    else:
        print("Invalid Input!")            

connection.close()
