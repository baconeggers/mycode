import time

try:
    u_beer = int(input("How many bottles of beer on the wall? "))

    if u_beer > 100:
        print("Please enter a number between 1 and 100")
    else:
        for beer in range(u_beer,0,-1):
            if beer == 1:
                print(f"{beer} bottle of beer on the wall!")
                print(f"{beer} bottle of beer! You take one down, pass it around!\n{beer - 1} bottles of beer on the wall!")
            else:
                print(f"{beer} bottles of beer on the wall!")
                print(f"{beer} bottles of beer! You take one down, pass it around!\n{beer - 1} bottles of beer on the wall!")
                time.sleep(0.1)
except:
    print("That wasn't a number, please try again!")