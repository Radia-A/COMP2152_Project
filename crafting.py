class Item:
    def __init__(self, name, item_type, quality="normal", durability=100):
        self.name = name
        self.type = item_type
        self.quality = quality
        self.durability = durability
        self.can_be_crafted = True

    def __str__(self):
        return f"{self.name} ({self.quality} quality, {self.durability}% durability)"

class CraftingSystem:
    def __init__(self):
        # Define basic items
        self.available_items = [
            Item("Red Herb", "herb", "normal"),
            Item("Blue Herb", "herb", "rare"),
            Item("Health Potion", "potion", "normal"),
            Item("Mana Potion", "potion", "rare"),
            Item("Iron Sword", "weapon", "normal"),
            Item("Steel Sword", "weapon", "rare")
        ]
        
        # Define crafting recipes
        self.recipes = {
            ("herb", "potion"): {
                "rare": "Super Healing Potion",
                "normal": "Basic Healing Potion"
            },
            ("herb", "weapon"): {
                "rare": "Poisoned Weapon",
                "normal": "Enchanted Weapon"
            },
            ("potion", "weapon"): {
                "rare": "Magical Weapon",
                "normal": "Blessed Weapon"
            }
        }

    def get_craftable_items(self, inventory):
        """Use list comprehension to filter craftable items from inventory"""
        return [item for item in inventory if item.can_be_crafted and item.durability > 0]

    def craft_items(self, primary_item, secondary_item):
        """Craft items using nested conditional statements"""
        if primary_item.type == "herb":
            if secondary_item.type == "potion":
                if primary_item.quality == "rare":
                    result = "Super Healing Potion"
                    print(f"Crafted a {result} using {primary_item.name} and {secondary_item.name}")
                else:
                    result = "Basic Healing Potion"
                    print(f"Crafted a {result} using {primary_item.name} and {secondary_item.name}")
            elif secondary_item.type == "weapon":
                if primary_item.quality == "rare":
                    result = "Poisoned Weapon"
                    print(f"Crafted a {result} using {primary_item.name} and {secondary_item.name}")
                else:
                    result = "Enchanted Weapon"
                    print(f"Crafted a {result} using {primary_item.name} and {secondary_item.name}")
        elif primary_item.type == "potion" and secondary_item.type == "weapon":
            if primary_item.quality == "rare":
                result = "Magical Weapon"
                print(f"Crafted a {result} using {primary_item.name} and {secondary_item.name}")
            else:
                result = "Blessed Weapon"
                print(f"Crafted a {result} using {primary_item.name} and {secondary_item.name}")
        else:
            result = None
            print("These items cannot be combined!")

        # Reduce durability of used items
        if result:
            primary_item.durability -= 20
            secondary_item.durability -= 20
            if primary_item.durability <= 0:
                primary_item.can_be_crafted = False
            if secondary_item.durability <= 0:
                secondary_item.can_be_crafted = False

        return result

    def display_inventory(self, inventory):
        """Display the current inventory with item details"""
        print("\nCurrent Inventory:")
        print("-" * 50)
        for item in inventory:
            print(f"- {item}")
        print("-" * 50)

# Example usage:
if __name__ == "__main__":
    # Create crafting system
    crafting = CraftingSystem()
    
    # Create a sample inventory
    inventory = [
        Item("Red Herb", "herb", "normal"),
        Item("Blue Herb", "herb", "rare"),
        Item("Health Potion", "potion", "normal"),
        Item("Iron Sword", "weapon", "normal")
    ]
    
    # Display initial inventory
    crafting.display_inventory(inventory)
    
    # Get craftable items
    craftable_items = crafting.get_craftable_items(inventory)
    print("\nCraftable Items:")
    for item in craftable_items:
        print(f"- {item}")
    
    # Try crafting some items
    print("\nAttempting to craft items...")
    result1 = crafting.craft_items(inventory[0], inventory[2])  # Red Herb + Health Potion
    result2 = crafting.craft_items(inventory[1], inventory[3])  # Blue Herb + Iron Sword
    
    # Display final inventory
    crafting.display_inventory(inventory) 