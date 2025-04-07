class WeaponProgression:
    def __init__(self):
        # Define available weapons and their requirements
        self.weapons = ["Dagger", "Sword", "Greatsword", "Legendary Blade"]
        self.weapon_requirements = {
            "Dagger": 0,
            "Sword": 3,
            "Greatsword": 6,
            "Legendary Blade": 9
        }
        self.weapon_stats = {
            "Dagger": 2,
            "Sword": 4,
            "Greatsword": 6,
            "Legendary Blade": 8
        }

    def get_available_weapons(self, monsters_killed):
        """Use list comprehension to get all weapons the hero can use based on monsters killed"""
        return [w for w in self.weapons if monsters_killed >= self.weapon_requirements[w]]

    def get_current_weapon(self, monsters_killed):
        """Get the best weapon available based on monsters killed using list comprehension"""
        available_weapons = self.get_available_weapons(monsters_killed)
        return available_weapons[-1] if available_weapons else self.weapons[0]

    def get_weapon_stats(self, weapon_name):
        """Get weapon stats using nested conditionals"""
        if weapon_name == "Legendary Blade":
            return {
                "damage": 8,
                "special_effect": "Critical Strike",
                "durability": 100
            }
        elif weapon_name == "Greatsword":
            return {
                "damage": 6,
                "special_effect": "Heavy Strike",
                "durability": 80
            }
        elif weapon_name == "Sword":
            return {
                "damage": 4,
                "special_effect": "Quick Strike",
                "durability": 60
            }
        else:  # Dagger
            return {
                "damage": 2,
                "special_effect": "None",
                "durability": 40
            }

    def upgrade_hero_weapon(self, hero, monsters_killed):
        """Upgrade hero's weapon based on monsters killed"""
        current_weapon = self.get_current_weapon(monsters_killed)
        weapon_stats = self.get_weapon_stats(current_weapon)
        
        # Update hero's combat strength based on new weapon
        hero.combat_strength = weapon_stats["damage"]
        
        print(f"\n    |    Weapon Upgrade!")
        print(f"    |    New Weapon: {current_weapon}")
        print(f"    |    Damage: {weapon_stats['damage']}")
        print(f"    |    Special Effect: {weapon_stats['special_effect']}")
        print(f"    |    Durability: {weapon_stats['durability']}%")
        
        return current_weapon 