BEGIN TRANSACTION;

DROP TABLE IF EXISTS Champions;
DROP TABLE IF EXISTS Lore;
DROP TABLE IF EXISTS Champion_Lore;
DROP TABLE IF EXISTS Skin_Lines;
DROP TABLE IF EXISTS Champion_Skins;
DROP TABLE IF EXISTS Items;
DROP TABLE IF EXISTS Champion_Items;

CREATE TABLE Champions (
    champion_name VARCHAR(255) PRIMARY KEY,
    abilities VARCHAR(255),
    date_released VARCHAR(255),
    difficulty VARCHAR(255)
);

CREATE TABLE Lore (
    lore_name VARCHAR(255) PRIMARY KEY
);

CREATE TABLE Champion_Lore (
    champion_name VARCHAR(255),
    lore_name VARCHAR(255),
    region VARCHAR(255) NOT NULL,
    PRIMARY KEY (champion_name, lore_name),
    FOREIGN KEY (champion_name) REFERENCES Champions(champion_name),
    FOREIGN KEY (lore_name) REFERENCES Lore(lore_name)
);

CREATE TABLE Skin_Lines (
    skin_series VARCHAR(255) PRIMARY KEY
);

CREATE TABLE Champion_Skins (
    champion_name VARCHAR(255),
    skin_series VARCHAR(255),
    skin_name VARCHAR(255) NOT NULL,
    PRIMARY KEY (champion_name, skin_series, skin_name),
    FOREIGN KEY (champion_name) REFERENCES Champions(champion_name),
    FOREIGN KEY (skin_series) REFERENCES Skin_Lines(skin_series)
);

CREATE TABLE Items (
    item_name VARCHAR(255) PRIMARY KEY,
    health INT,
    attack_damage INT,
    attack_speed FLOAT,
    armor INT,
    magic_resist INT,
    movement_speed INT
);

CREATE TABLE Champion_Items (
    champion_name VARCHAR(255),
    item_name VARCHAR(255),
    common_item BOOLEAN,
    damage_type VARCHAR(255),
    PRIMARY KEY (champion_name, item_name),
    FOREIGN KEY (champion_name) REFERENCES Champions(champion_name),
    FOREIGN KEY (item_name) REFERENCES Items(item_name)
);

END TRANSACTION

