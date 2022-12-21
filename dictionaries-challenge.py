#!/usr/bin/env python3

marvelchars= {
"Starlord":
    {"real name": "Peter Quill",
    "power": "Dance Moves",
    "archenemy": "Thanos"},

"Mystique":
    {"real name": "Raven Darkholme",
    "power": "Shape Shifter",
    "archenemy": "Professor X"},

"Hulk":
    {"real name": "Bruce Banner",
    "power": "Super Strength",
    "archenemy": "Adrenaline"},
                }

char_name = input("Which character do you want to know about? (Starlord, Mystique, Hulk) ")
char_stat = input("Which statistic do you want to know about? (Real Name, Power, Archenemy) ")

char_name = char_name.title()
char_stat = char_stat.lower()

print(char_name + "\'s", char_stat, "is: " + marvelchars[char_name][char_stat].title())