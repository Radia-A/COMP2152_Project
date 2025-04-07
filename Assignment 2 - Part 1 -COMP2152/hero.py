# hero.py (Hero Class)
from character import Character

class Hero(Character):
    def __init__(self, level=1):
        super().__init__()
        self.level = level  # ✅ Add level attribute

    def hero_attacks(self, monster):
        print(f"Hero attacks Monster ({monster.health_points}) with strength {self.combat_strength}")

        if self.combat_strength >= monster.health_points:
            monster.health_points = 0
            print("The Hero has defeated the Monster!")
        else:
            monster.health_points -= self.combat_strength
            print(f"Monster's health reduced to: {monster.health_points}")

        return monster.health_points
