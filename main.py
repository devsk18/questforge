from domain.character import Character


if __name__ == "__main__":
    hero = Character("Aria", 100, 30)
    goblin = Character("Goblin", 50, 15)
    villain = Character("Devil", 150, 40)

    print("--- Initial State ---")
    print(hero.describe())
    print(goblin.describe())
    print(villain.describe())

    print("\n--- Battle Begins ---")
    hero.attack(goblin)
    villain.attack(hero)
    goblin.attack(villain)

    print("\n--- After First Round ---")
    print(hero.describe())
    print(goblin.describe())
    print(villain.describe())

    hero.attack(villain)
    villain.attack(goblin)
    goblin.attack(hero)

    print("\n--- After Second Round ---")
    print(hero.describe())
    print(goblin.describe())
    print(villain.describe())

    hero.attack(villain)
    villain.attack(hero)
    hero.heal(50)

    print("\n--- After Healing ---")
    print(hero.describe())
    print(goblin.describe())
    print(villain.describe())

    print("\n--- Final Round ---")
    hero.attack(villain)
    villain.attack(hero)
    hero.attack(villain)
    hero.heal(30)

    print("\n--- Final State ---")
    print(hero.describe())
    print(goblin.describe())
    print(villain.describe())