# pythonSQLWRAPPER
A short example of how a python wrapper can be used to execute sql queries 

Folder includes:
sqlite3 Database: a6\LOL.db 
the user interface code: a6\LOL.py
Database initializer: a6\initDatabase.sql
ER Diagram: ER_Diagram.png

Notes:
In LOL.py
- "fillDB()" is used to inject the code with Test Data

Database’s Brief Description:
This Database is about listing all the League Of Legend Characters and their details, this
database is intended to provide users with a source of knowledge for Characters they may not
know of in the hit game League of Legends. I chose to make this database as when I was a new
League of Legends player, it was difficult to know all these details of these characters when I
was going against them in the game. This Database is intended to be used like a separate
window that you may access while playing league of legends to understand the characters while
in the game.
The application aims to:
1. Provide a database that contains all the characters in League of Legends, Items and
other information.
2. Allow updatable information as old/new characters or lore
3. Enables searching and filtering characters by the name of their Lore and vice versa
4. The size of this database should be able to contain all current characters as well as have
space for possible future characters.
My intention with the relationships is demonstrated below:
[champion_name|abilities,date_released,difficulty,Chealth,Cattack_damage,Cattack_spee
d,Carmor,Cmagic_resist,Cmovement_speed,resource_type]
[champion_name,skin_series | skin_name]
[lore_name,champion_name | region]
[item_name,champion_name | common_item,damage_type]
[Item_name|Ihealth,Iattack_damage,Iattack_speed,Iarmor,Imagic_resist,Imovement_spee
d]


