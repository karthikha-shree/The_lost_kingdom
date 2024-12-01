class Player:
    def __init__(self):
        self.inventory = {}
        self.health = 100

    def take_damage(self, amount):
        self.health -= amount
        print(f"You took {amount} damage. Health: {self.health}")
        if self.health <= 0:
            print("You have succumbed to the dangers of Arthenis.")
            # End game here or add restart logic

    def heal(self, amount):
        self.health += amount
        print(f"You regained {amount} health. Health: {self.health}")
    def add_to_inventory(self, item, description):
        self.inventory[item] = description
        print(f"{item} has been added to your inventory.")

    def has_item(self, item):
        return item in self.inventory

    def show_inventory(self):
        if self.inventory:
            print("Your inventory contains:")
            for item, description in self.inventory.items():
                print(f"- {item}: {description}")
        else:
            print("Your inventory is empty.")

    def examine_item(self, item):
        if item in self.inventory:
            print(f"{item}: {self.inventory[item]}")
        else:
            print(f"{item} is not in your inventory.")
