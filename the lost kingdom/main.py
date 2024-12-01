from player import Player
from story import start_story
from locations import enter_whispering_woods, enter_abandoned_village, enter_crystal_caverns, enter_lost_castle
from save_load import save_game, load_game


def game_loop():
    print("Welcome to The Lost Kingdom of Arthenis!")
    player = Player()
    start_story()

    while True:
        print("\nWhere would you like to go?")
        print("1. Whispering Woods")
        print("2. Abandoned Village")
        print("3. Crystal Caverns")
        print("4. Lost Castle")
        print("5. Check Inventory")
        print("6. Save Game")
        print("7. Load Game")
        print("8. Examine an Item")
        print("9. Quit")

        choice = input("Choose an option: ")

        if choice == "1":
            enter_whispering_woods(player)
        elif choice == "2":
            enter_abandoned_village(player)
        elif choice == "3":
            enter_crystal_caverns(player)
        elif choice == "4":
            enter_lost_castle(player)
        elif choice == "5":
            player.show_inventory()
        elif choice == "6":
            save_game(player)
        elif choice == "7":
            load_game(player)
        elif choice == "8":
            item_name = input("Enter the name of the item you want to examine: ")
            player.examine_item(item_name)
        elif choice == "9":
            print("Thank you for playing!")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    game_loop()
