import time
import random
items = []


scenarios = [" a loud heavy roar, almost dinosaur like",
             " high pitch screeching, and the sound of wings going by "
             "your window.",
             " church bells ringing for a few second then a loud "
             "explosion and the bells stop."]

random_scenario = random.choice(scenarios)


def print_pause(text):
    print(text)
    time.sleep(1)


def intro():
    print_pause("You wake up in your city apartment.")
    print_pause("Something seems different.")
    print_pause("Unknown to you supernatural and mystical creatures"
                " have taken over the city, maybe the world.")
    print_pause(f"You hear{random_scenario}")
    print_pause("You look around your apartment for something to protect"
                " yourself.")


def first_weapon(items):
    print_pause("What will you choose...\n")
    first_choice = input("1.Shotgun\n"
                         "2.Baseball bat\n")
    if first_choice == '1':
        print_pause("You grab your shotgun and head outside")
        items.append("shotgun")

    elif first_choice == '2':
        print_pause("You grab the baseball bat and head outside")
        items.append("baseball bat")

    else:
        print_pause("Sorry I dont recognise that choice, please try"
                    " again.")
        first_weapon(items)


def st_choice(items):
    print_pause("After a few miles of walking you come to a fork.")
    print_pause("To the left will lead you to where you heard the"
                " noise.")
    print_pause("To the right will lead you down a dark unknown road.")
    print_pause("right or left")

    direction = input("What way will you go?\n")
    if "right" in direction:
        go_right(items)

    elif "left" in direction:
        go_left(items)
    else:
        print_pause("Sorry I do not understand")
        st_choice(items)


def go_right(items):

    if "shotgun" in items:
        print_pause("After a few miles, you see a man being attack"
                    " by a creature...")
        print_pause("It's a vampire!")
        print_pause("You pull out your shotgun and shoot the vampire,"
                    " it hits and the vampire is left laying on the ground")
        print_pause("you approach the body and the man...")
        print_pause("Suddenly the vampire lunges at you, grabs you, and sinks"
                    " its teeth into your neck")
        print_pause("You are left lieing in the street slowly dying.")
        play_again()

    elif "baseball bat" in items:
        print_pause("After a few miles, you see a man being attack"
                    " by a creature...")
        print_pause("It's a vampire!")
        print_pause("You rush in swing your bat it breaks in the"
                    " center.")
        print_pause("The vampire turns and lunges at you.")
        print_pause("You thrust the broken bat into its chest and the"
                    " vampire, burst into  flames then turns to dust.")
        print_pause("He offers you a choice three different pistols"
                    " each with one shot.")
        items.remove("baseball bat")
        second_weapons(items)

    elif "ice pistol" or "ice pistol" or "sun pistol" in items:
        print_pause("Now a dead end...")
        st_choice(items)


def second_weapons(items):
    pistol_choice = input("1.One that shoots a bullet of magical ice.\n"
                          "2.One that shoots a bullet made from light of"
                          " the sun.\n"
                          "3.One made of a bullet blessed by a holy priest\n")
    if "1" in pistol_choice:
        print_pause("You take the ice pistol and head back.")
        items.append("ice pistol")
        st_choice(items)
    elif "2" in pistol_choice:
        print_pause("You take the sun pistol and head back.")
        items.append("sun pistol")
        st_choice(items)
    elif "3" in pistol_choice:
        print_pause("You take the holy pistol and head back.")
        items.append("holy pistol")
        st_choice(items)
    else:
        print_pause("Sorry not a valid choice.")
        second_weapons(items)


def go_left(items):
    print_pause("You turn left, a few files down the road you see what"
                " was responsible for the sound you heard from your apartment")
    if "dinosaur" in random_scenario:
        print_pause("A fire wyvern rushes towards you...")
        if "shotgun" in items:
            print_pause("As it gets closer you take your shot with"
                        " the shotgun.")
            print_pause("The monster is briefly stunned.")
            print_pause("You turn and run for it, as you run away you see a"
                        " baseball bat laying next to a pile of trash")
            print_pause("You pick up the bat and head back")
            items.append("baseball bat")
            items.remove("shotgun")
            st_choice(items)

        elif "baseball bat" in items:
            print_pause("You swing the bat but it has no affect")
            print_pause("The fire wyvern raises it's head and exhales a blast"
                        " of scorching hot flames onto you...")
            print_pause("You were defeated")
            play_again(items)

        elif "ice pistol" in items:
            print_pause("You take your shot with the ice pistol")
            print_pause("It hits the fire wyvern in the skull.")
            print_pause("The wyvern skin turns to ice and shatters")
            print_pause("The monster has been defeated but what else"
                        " will you run into?")
            play_again()

        elif "sun pistol" in items:
            print_pause("You take your shot with the sun pistol, but it has"
                        " no affect")
            print_pause("The fire wyvern raises it's head and exhales a blast"
                        " of scorching hot flames onto you...")
            print_pause("You were defeated")
            play_again()

        elif "holy pistol" in items:
            print_pause("You take your shot with the holy pistol, but it"
                        " has no affect")
            print_pause("The fire wyvern raises it's head and exhales a blast"
                        " of scorching hot flames onto you...")
            print_pause("You were defeated")
            play_again()

    elif "church" in random_scenario:
        print_pause("A giant demon stand infront of you...")
        if "shotgun" in items:
            print_pause("As it gets closer you take your shot with the"
                        " shotgun.")
            print_pause("The monster is briefly stunned.")
            print_pause("You turn and run for it, as you run away you see"
                        " a baseball bat laying next to a pile of trash")
            print_pause("You pick up the bat and head back")
            items.append("baseball bat")
            items.remove("shotgun")
            st_choice(items)

        elif "baseball bat" in items:
            print_pause("You swing the bat but it has no affect")
            print_pause("The demon picks you up and smashed your head"
                        " with one blow")
            print_pause("You were defeated")
            play_again()

        elif "ice pistol" in items:
            print_pause("You take your shot with the ice pistol,"
                        " but it has no affect")
            print_pause("The demon picks you up and smashed your head"
                        " with one blow")
            print_pause("You were defeated")
            play_again()

        elif "sun pistol" in items:
            print_pause("You take your shot with the sun pistol,"
                        " but it has no affect.")

            print_pause("The demon picks you up and smashed your"
                        " head with one blow")
            print_pause("You were defeated")
            play_again()

        elif "holy pistol" in items:
            print_pause("You take your shot with the sun pistol.")
            print_pause("The demon is hit square in the head")
            print_pause("It roars one last time as it turns into"
                        " dust")
            print_pause("The monster has been defeated but what else"
                        " will you run into?")
            play_again()

    elif "screech" in random_scenario:
        print_pause("Behold your eyes it's Dracula...")
        if "shotgun" in items:
            print_pause("As it gets closer you take your shot with"
                        " the shotgun.")
            print_pause("The monster is briefly stunned.")
            print_pause("You turn and run for it, as you run away,"
                        " you see a baseball bat laying next to"
                        " a pile of trash")
            print_pause("You pick up the bat and head back")
            items.append("baseball bat")
            items.remove("shotgun")
            st_choice(items)

        elif "baseball bat" in items:
            print_pause("You swing the bat but it has no affect")
            print_pause("Dracule easily grabs you and bites"
                        " your neck")
            print_pause("You were defeated")
            play_again()

        elif "ice pistol" in items:
            print_pause("You take your shot with the ice pistol,"
                        " but it has no affect")
            print_pause("The bull has no affect...")
            print_pause("Dracule easily grabs you and bites"
                        " your neck")
            print_pause("You were defeated")
            play_again()

        elif "sun pistol" in items:
            print_pause("You take your shot with the sun pistol.")
            print_pause("Dracula is hit in the chest and lunges"
                        " for you but burst into flames")
            print_pause("The monster has been defeated but what"
                        " else will you run into?")
            play_again()

        elif "holy pistol" in items:
            print_pause("You take your shot with the sun pistol.")
            print_pause("Dracule easily grabs you and bites"
                        " your neck")
            print_pause("You were defeated")
            play_again()


def play_again():
    items.clear()
    next_game = input("Would you like to play again?\n Yes or No\n")
    if "yes" in next_game:
        play_game(items)

    elif "no" in next_game:
        print_pause("Thanks for playing!")

    else:
        print_pause("Sorry not I do not understand.")
        play_again()


def play_game(items):
    intro()
    first_weapon(items)
    st_choice(items)


play_game(items)
