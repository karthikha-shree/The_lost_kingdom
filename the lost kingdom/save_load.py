import json

def save_game(player):
    game_data = {
        "inventory": player.inventory,
        "health": player.health
    }
    with open("save_file.json", "w") as file:
        json.dump(game_data, file)
    print("Game saved.")

def load_game(player):
    try:
        with open("save_file.json", "r") as file:
            game_data = json.load(file)
            player.inventory = game_data["inventory"]
            player.health = game_data["health"]
        print("Game loaded.")
    except FileNotFoundError:
        print("No saved game found.")
