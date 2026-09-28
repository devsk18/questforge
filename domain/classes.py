from mimetypes import init

from domain.character import Character

class Warrior(Character):
    def __init__(self, name: str) -> None:
        super().__init__(name, health=120, attack_power=18)

    def special_ability(self, target: Character) -> None:
        damage = int(self.attack_power * 1.5)
        target.take_damage(damage)
        print(f"{self.name} uses cleave! {damage} damage to {target.name}")


class Mage(Character):
    def __init__(self, name: str) -> None:
        super().__init__(name, health=80, attack_power=10)
        self.__mana = 50

    @property
    def mana(self) -> int:
        return self.__mana

    def special_ability(self, target: Character) -> None:
        cost = 20
        if self.mana < cost:
            print(f"{self.name} doesn't have enough mana!")
            return
        damage = int(self.attack_power * 3)
        target.take_damage(damage)
        print(f"{self.name} casts Fireball! {damage} damage to {target.name}")


class Rogue(Character):
    def __init__(self, name: str) -> None:
        super().__init__(name, health=90, attack_power=14)

    def special_ability(self, target: Character) -> None:
        damage = int(self.attack_power * 2)
        target.take_damage(damage)
        print(f"{self.name} casts Fireball! {damage} damage to {target.name}")

class Cleric(Character):
    def __init__(self, name: str) -> None:
        super().__init__(name, health=50, attack_power=5)
        self.__heal_power = 20

    def special_ability(self, target: Character) -> None:
        target.heal(int(self.__heal_power * 1.5))