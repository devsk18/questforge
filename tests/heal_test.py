from domain.character import Character

max_health = 100
hero = Character("Aria", max_health, 30)
print(hero.describe())
hero.heal(50)

if hero.health == max_health:
    print("Test passed: Health is capped at max health.")


# run using : python -m tests.heal_test