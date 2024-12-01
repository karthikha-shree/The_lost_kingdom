from puzzles import solve_tree_riddle, solve_abandoned_village_puzzle, solve_crystal_caverns_puzzle, solve_castle_puzzle
from npcs import speak_to_old_wanderer
import random

def enter_whispering_woods(player):
    print("\nYou enter the Whispering Woods. The trees seem to whisper secrets...")

    # 50% chance of encountering a forest creature
    if random.random() < 0.5:
        print("A wild creature attacks!")
        player.take_damage(20)

    print("1. Explore the ancient tree\n2. Follow the faint path\n3. Talk to the old wanderer")
    choice = input("What would you like to do? ")

    if choice == "1":
        solve_tree_riddle(player)
    elif choice == "2":
        print("The path leads you to a hidden clearing with mysterious carvings on the stones.")
    elif choice == "3":
        speak_to_old_wanderer(player)
    else:
        print("Invalid choice.")

    if not player.has_item("lost charm"):
        print("You stumble upon a shiny object under a tree. It's a lost charm!")
        player.add_to_inventory("lost charm", "An old charm belonging to the wanderer.")


def enter_abandoned_village(player):
    print("\nYou arrive at the Abandoned Village, a place haunted by the past.")
    print("1. Examine the broken stone tablet\n2. Explore the abandoned houses")
    choice = input("What would you like to do? ")

    if choice == "1":
        solve_abandoned_village_puzzle(player)
    elif choice == "2":
        print("You search the abandoned houses, finding remnants of old lives, but nothing else of value.")
    else:
        print("Invalid choice.")


def enter_crystal_caverns(player):
    print("\nThe Crystal Caverns shimmer with an eerie light.")
    print("1. Examine the glowing crystals\n2. Explore deeper into the caverns")
    choice = input("What would you like to do? ")

    if choice == "1":
        solve_crystal_caverns_puzzle(player)
    elif choice == "2":
        print("You explore deeper into the caverns, but the glowing crystals seem to be the main mystery here.")
    else:
        print("Invalid choice.")


def enter_lost_castle(player):
    print("\nYou stand before the Lost Castle of Arthenis.")

    # Check if the player has the key items required to enter the castle
    if player.has_item("ancient map piece") and player.has_item("old amulet") and player.has_item("magical key"):
        print("The items resonate, unlocking the castle's hidden door.")
        print("You proceed inside and encounter a final test.")
        solve_castle_puzzle(player)

        # Check for the "Heart of Arthenis" item
        if player.has_item("heart of arthenis"):
            # Good ending if the player also has the optional side quest item "mysterious gem"
            if player.has_item("mysterious gem"):
                print("\nYou hold the Heart of Arthenis and the Mysterious Gem.")
                print("A brilliant light surrounds you as the castle and kingdom are fully restored!")
                print(
                    "Congratulations! You have completed your journey and lifted the curse, restoring Arthenis to glory!")
                print("The people of Arthenis remember you as their hero for generations to come.")
            else:
                print("\nWith the Heart of Arthenis in hand, you lift the curse over the kingdom.")
                print("However, without the Mysterious Gem, Arthenis remains only a shadow of its former self.")
                print("Though the curse is broken, the kingdom remains quiet and empty.")
        else:
            # Neutral ending if the player reached the castle but didn't find the Heart of Arthenis
            print("\nYou reach the end of your journey but could not find the Heart of Arthenis.")
            print("The curse remains upon the kingdom, and you become a part of its legend.")
            print("Perhaps another adventurer will succeed where you could not.")
    else:
        # If the player does not have the required items, they cannot enter the castle
        print("The castle’s door remains closed. Perhaps there are items you still need to collect.")
