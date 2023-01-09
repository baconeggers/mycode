#!/usr/bin/env python3

import requests

MAJORTOM = "http://api.open-notify.org/astros.json"

def main():
    groundctrl = requests.get(MAJORTOM)

    helmetson = groundctrl.json()

    print("\n\nConverted Python Data")
    #print(helmetson)

    print("\n\nPeople in Space: ", helmetson['number'])
    #people = helmetson['people']
    #print(people)

    for nauts in helmetson['people']:
        print(f"{nauts['name']} is on the {nauts['craft']}")

if __name__ == "__main__":
    main()