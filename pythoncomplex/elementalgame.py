# Printing version

print("V:BETA1")

# Importing Modules
import time
import lev2
score = 0
#  Dictionary of elements and their charge
elements = {'Hydrogen':-1}

# Room Definitions
def room1lev1():
    print("""This is the helium room. Nothing valuable here. By the way your water level is going down.
    Air level is fine. Think about what you can do. Oxygen is required for breathing, I think. The tablet will ask you something.
    """)
    tablet1 = input("What to do, sir? 1 for abort, 2 for gas pump to take the air in, 3 for going to another room:")
    if tablet1 == "1":
        exit()
    elif tablet1 == "2":
        print('Taken in sir. Oxygen levels inside the pump is high. H20 can now be made.')
        time.sleep(4)
        print('H20 MADE. READY. WATER LEVELS: FINE. DISCOVERED TWO NEW ELEMENTS, OXYGEN AND HELIUM.')
        elements["Helium"] = 0
        elements["Oxygen"] = -2
        lev2.room1(elements)
def room2lev1():
    print("Nitrogen suffocation.  You died. Exiting game....")
    time.sleep(5)
    exit()
def room3lev1():
    print("Suprise! You have discovered lithium! But it exploded. Your health is low. Water level:low Air Level: High")
    disc = input('What do you want to do 1 for explore 2 for moving on 3 for mixing lithium and hydrogen:')
    if disc == "1":
        print("You discovered Oxygen.")
        elements["Lithium"] = +1
        elements["Oxygen"] = -2
        lev2.room2(elements)
    elif disc == "2":
        print("OK then.")
        elements["Lithium"] = +1
        lev2.room2(elements)
    elif disc == "3":
        print("You died. Exiting....")
        time.sleep(5)
        exit()

def start(points):
    elements = {'Hydrogen':'+1'}
    print("""At the first you have element hydrogen. The properties of Hydrogen are 
    1.Flammable
    2.Fusionable
    3.Charge: Wants one electron.
    """)
    print("That's the information. Now select one room. Room 1 or Room2 or Room 3:")
    roomlev1=input("")
    if roomlev1 == "1":
        room1lev1()
    elif roomlev1 == "2":
        room2lev1()
    elif roomlev1 == '3':
        room3lev1() 
    else:
        second = input("please enter a correct digit:" )
        if second == "1":
            room1lev1()
        elif second == "2":
            room2lev1()
        elif second == '3':
            room3lev1() 
        else:
            exit()
# Starting Code
while True:
        print(""""
        Welcome to the elemental sandbox. This is a game where you get to know about the elements
        and their properties. Feel free to explore different parts of the code. Hacking is discouraged and there is a counter measure
        against it. I will be happy if you contribute to this game. Press s to start and x to exit.
        """)
        dec = input(":")
        if dec == "s":
            if score == 0:
                start(score)
            else:
                print("Aborting, you have cheated. ")
                time.sleep(5)
                exit()







    
        



