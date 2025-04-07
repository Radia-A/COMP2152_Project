from hero import Hero
from monster import Monster


def spawn_adaptive_monsters(hero):
    monsters = [Monster() for _ in range(hero.level)]

    for monster in monsters:
        if hero.level < 5:
            monster.health_points = 50
            monster.combat_strength = 10
        elif hero.level < 10:
            monster.health_points = 100
            monster.combat_strength = 20
        else:
            monster.health_points = 150
            monster.combat_strength = 30

    return monsters


if __name__ == "__main__":
    # You can change the hero's level here to test different scenarios
    hero = Hero(level=3)

    print(f"Hero created with {hero.combat_strength} combat strength and {hero.health_points} HP (Level {hero.level})")

    # Spawn adaptive monsters
    monsters = spawn_adaptive_monsters(hero)
    print(f"\nSpawning {len(monsters)} monster(s) based on hero level...")

    for i, monster in enumerate(monsters, start=1):
        print(f"\n⚔️  Battle {i}: Monster with {monster.combat_strength} ATK and {monster.health_points} HP")
        hero.hero_attacks(monster)
        if monster.health_points > 0:
            monster.monster_attacks(hero)

        if hero.health_points <= 0:
            print("💀 Hero has died. Game Over.")
            break

    if hero.health_points > 0:
        print("\n🏆 Hero survived all battles!")
    else:
        print("\n☠️ Hero was defeated during the battles.")
