class Character:
    def __init__(self, name: str, health: int, attack_power: int) -> None:
        self.name = name
        self.health = health
        self.max_health = health
        self.attack_power = attack_power

    def attack(self, target: Character) -> None:
        target.health -= self.attack_power
        print(f"{self.name} attacks {target.name} for {self.attack_power} damage!")
        if target.health <= 0:
            target.health = 0
            print(f"{self.name} killed {target.name}!")

    def heal(self, heal_point: int) -> None:
        self.health += heal_point
        if self.health > self.max_health:
            self.health = self.max_health
        print(f"{self.name} got {heal_point} heal points! - Health: {self.health}")

    def describe(self) -> str:
        if self.health <= 0:
            return f"{self.name} is dead."
        return f"{self.name} has {self.health} HP and {self.attack_power} ATK"

            
