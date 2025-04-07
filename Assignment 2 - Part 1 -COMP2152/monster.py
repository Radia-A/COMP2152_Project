# monster.py (Monster Class)
from character import Character


class Monster(Character):
    def __init__(self):
        super().__init__()

    def monster_attacks(self, hero):
        print(f"Monster attacks Hero ({hero.health_points}) with strength {self.combat_strength}")
        if self.combat_strength >= hero.health_points:
            hero.health_points = 0
            print("Monster has defeated the hero!")
        else:
            hero.health_points -= self.combat_strength
            print(f"Hero's health is now {hero.health_points}")

    def __del__(self):
        print("The Monster object is being destroyed by the garbage collector")
        super().__del__()




if __name__ == "__main__":
    monster = Monster()  # Assuming Monster class exists
    print(f"Monster created with {monster.combat_strength} combat strength and {monster.health_points} HP")
