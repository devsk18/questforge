from domain.battle import run_special_round, total_party_damage
from domain.character import Character
from domain.classes import Cleric, Mage, Rogue, Warrior


if __name__ == "__main__":
    party = [Warrior("Bram"), Mage("Sylla"), Rogue("Kade"), Cleric("Healer")]
    dummy = Warrior("Dummy")
    
    for member in party:
        run_special_round(member, dummy)
        print(f"Dummy HP: {dummy.health}\n")

    total_party_damage(party, dummy)
    dummy.describe()
    
    
    """ 
    warrior = Warrior("Bram")
    mage = Mage("Sylla")
    rogue = Rogue("Devil")
    cleric = Cleric("Healer")

    print("--- Initial State ---")
    warrior.describe()
    mage.describe()
    rogue.describe()
    cleric.describe()

    print("\n--- Battle Begins ---")
    warrior.attack(mage)
    rogue.attack(warrior)
    mage.attack(rogue)
    cleric.special_ability(warrior)

    print("\n--- After First Round ---")
    warrior.describe()
    mage.describe()
    rogue.describe()
    cleric.describe()

    print("\n--- Second Round: Special Moves ---")
    warrior.special_ability(mage)
    rogue.special_ability(warrior)
    mage.special_ability(rogue)
    cleric.special_ability(mage)

    print("\n--- After Second Round ---")
    warrior.describe()
    mage.describe()
    rogue.describe()
    cleric.describe()

    print("\n--- Final Exchange ---")
    warrior.attack(rogue)
    rogue.attack(mage)
    mage.attack(warrior)
    cleric.special_ability(warrior)

    print("\n--- Final State ---")
    warrior.describe()
    mage.describe()
    rogue.describe()
    cleric.describe() 
    """
