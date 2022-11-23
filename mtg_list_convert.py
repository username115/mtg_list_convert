#! /usr/bin/python3

import csv
import sys
from unicodedata import name

#assume we are converting a Delver Lens export in Tappedout format with Collector's Number appended
#these files don't have headers

colnames = ['qty', 'name', 'set_code', 'set_name', 'language', 'condition', 'foil_qty', 'multiverse_id', 'card_num']

#Delver Lens name : Tappedout name
set_corrections = {
    'Secret Lair Drop':'Secret Lair',
    'Crimson Vow Commander':'Innistrad: Crimson Vow Commander',
    'Adventures in the Forgotten Realms':'Dungeons & Dragons: Adventures in the Forgotten Realms',
    'Midnight Hunt Commander':'Innistrad: Midnight Hunt Commander',
    'Universes Within':'Secret Lair: Universes Within',
    'Magic 2010':'2010 Core Set',
    'Magic 2011':'2011 Core Set',
    'Wizards Play Network 2010':'Promo Set',
    'Wizards Play Network 2022':'Promo Set',
    'Gatecrash Promos':'Promo Set',
    'Mystery Booster Playtest Cards 2021':'Mystery Booster: Convention Edition',
    'Innistrad: Crimson Vow Promos':'Innistrad: Crimson Vow',
    'Commander 2011':'MTG: Commander',
    'Forgotten Realms Commander':'Adventures in the Forgotten Realms: Commander',
    'Forgotten Realms Commander Display Commanders':'Adventures in the Forgotten Realms: Commander',
    "Dragon's Maze Promos":'Promo Set',
    'Friday Night Magic 2011':'Promo Set',
    'Magic 2014 Promos':'Promo Set',
    'Neon Dynasty Commander':'Kamigawa: Neon Dynasty Commander',
    'New Capenna Commander':'Streets of New Capenna: Commander',
    'Magic 2012':'2012 Core Set',
    'Modern Masters 2017':'Modern Masters 2017 Edition',
    "Commander Legends: Battle for Baldur's Gate Promos":"Commander Legends: Battle for Baldur's Gate",
    "Battle for Baldur's Gate Promos":"Commander Legends: Battle for Baldur's Gate",
    'Duel Decks Anthology: Garruk vs. Liliana':'Duel Decks: Garruk vs. Liliana',
    'Kamigawa: Neon Dynasty Promos':'Kamigawa: Neon Dynasty',
    'Zendikar Rising Commander':'Zendikar Rising: Commander',
    'Strixhaven Mystical Archive':'Strixhaven: Mystical Archive',
    'Strixhaven: School of Mages':'Strixhaven',
    'Modern Event Deck 2014':'Modern Event Deck',
    'Dominaria United Commander':'Dominaria United: Commander',
    'The Brothers\' War Retro Artifacts':'The Brothers\' War: Retro Artifacts',
    'The Brothers\' War Commander':'The Brothers\' War: Commander',
    'Transformers':'Universes Beyond: Transformers'
}

#Delver Lens name : Tappedout name
name_corrections = {
    'Wolf in _____ Clothing':'Wolf in ________ Clothing'
}

#fix missing language
language_corrections = {
        '':'English'
}


with open(sys.argv[1], newline='') as csvin:
    with open(sys.argv[2], 'w', newline='') as csvout:
        reader = csv.DictReader(csvin, fieldnames=colnames, delimiter=',', quotechar='"')
        writer = csv.DictWriter(csvout, fieldnames=colnames, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
        next(reader, None)
        for row in reader:
            if row['set_name'] in set_corrections:
                row['set_name'] = set_corrections[row['set_name']]
            if row['name'] in name_corrections:
                row['name'] = name_corrections[row['name']]
            if row['language'] in language_corrections:
                row['language'] = language_corrections[row['language']]
            writer.writerow(row)



