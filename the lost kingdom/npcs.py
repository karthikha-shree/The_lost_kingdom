def speak_to_old_wanderer(player):
    print("""
    Old Wanderer: 'Ah, another seeker of Arthenis? Many have come, few return.
    Remember, the trees hold memories of those who listen.'
    """)
    if not player.has_item("old coin"):
        player.add_to_inventory("old coin")
        print("The wanderer hands you an old coin, whispering, 'This might be useful on your journey.'")
    else:
        print("The wanderer nods at you, having nothing more to offer.")
def side_quest_old_wanderer(player):
    print("Old Wanderer: 'Can you find my lost charm? It is somewhere in the Whispering Woods.'")
    if player.has_item("lost charm"):
        print("Old Wanderer: 'You found it! Here, take this in return.'")
        player.add_to_inventory("mysterious gem", "A gem that seems to have some magical property.")
    else:
        print("The old wanderer looks around, awaiting the return of his charm.")
