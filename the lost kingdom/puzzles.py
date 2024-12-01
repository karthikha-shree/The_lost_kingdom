def solve_tree_riddle(player):
    attempts = 0
    while True:
        print("You find an inscription on the tree that reads:")
        print("'I speak without a mouth and hear without ears. What am I?'")
        answer = input("Your answer: ").strip().lower()
        attempts += 1

        if answer == "echo":
            print("Correct! The tree reveals a hidden compartment with an ancient map piece.")
            player.add_to_inventory("ancient map piece", "A fragment of a map, etched with symbols. It may reveal hidden paths.")
            break
        else:
            print("Incorrect.")
            if attempts >= 3:
                print("Hint: It’s something you hear in empty places.")


def solve_abandoned_village_puzzle(player):
    print("In the Abandoned Village, you find a broken stone tablet with an inscription:")
    print("'I am not alive, but I grow; I don’t have lungs, but I need air. What am I?'")
    answer = input("Your answer: ").strip().lower()

    if answer == "fire":
        print("Correct! The tablet glows, revealing an old amulet.")
        player.add_to_inventory("old amulet")
    else:
        print("Incorrect. Try again.")


def solve_crystal_caverns_puzzle(player):
    print("In the Crystal Caverns, you find a strange arrangement of crystals.")
    print("Each crystal emits a different sound when touched.")
    print("The inscription reads: 'Play the melody of the kingdom's rise.'")

    # Sequence for the puzzle (could be modified to make more complex)
    melody_sequence = ["do", "re", "mi", "fa"]
    player_sequence = []

    while player_sequence != melody_sequence:
        note = input("Touch a crystal and play a note (do, re, mi, fa): ").strip().lower()
        player_sequence.append(note)

        # Check if the sequence is correct as you go
        if player_sequence == melody_sequence:
            print("The crystals resonate in harmony, revealing a magical key.")
            player.add_to_inventory("magical key")
            break
        elif not melody_sequence[:len(player_sequence)] == player_sequence:
            print("The melody sounds incorrect. Try again.")
            player_sequence = []  # Reset the sequence if incorrect


def solve_castle_puzzle(player):
    print("Inside the castle, you face a final challenge.")
    print("A ghostly voice asks you: 'What is stronger than steel yet can be shattered with a single word?'")
    answer = input("Your answer: ").strip().lower()

    if answer == "silence":
        print("Correct! The spirit of Arthenis acknowledges your wisdom.")
        player.add_to_inventory("heart of arthenis")
    else:
        print("Incorrect. You feel a chilling wind as you try to answer again.")
