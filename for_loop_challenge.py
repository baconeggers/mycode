farms = [{"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
         {"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]},
         {"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]}]

def main():
    choice = input("Please choose a farm:\nNE Farm\nW Farm\nSE Farm\n").lower()

    if choice == "ne farm":
        choice_int = 0
    elif choice == "w farm":
        choice_int = 1
    elif choice == "se farm":
        choice_int = 2
    else:
        print("That was not a valid option, please try again.")

    choice_2 = input("Would you like to see just animals, or plants and animals?\nPlease enter 'Animals' or 'Both'\n").lower()

    if choice_2 == "animals":
        for animal in farms[choice_int].values():
            if animal not in ["carrots", "celery"]:
                print("\n",animal)
    elif choice_2 == "both":
        for animal in farms[choice_int].values():
            print("\n",animal) 


if __name__ == "__main__":
    main()