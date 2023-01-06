#!/usr/bin/env python3

import os

os.chdir("/home/student/mycode/Dracula")

count_count = 0

with open("dracula.txt","r") as drac:
    for line in drac:
        #print(line)
        if "vampire" in line.lower():
            print(line)
            count_count += 1
            with open("vampytimee.txt","a") as vampy:
                vampy.write(line)
print(count_count)