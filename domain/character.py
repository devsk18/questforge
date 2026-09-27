class Character:
    def __init__(self, name: str, health: int, attack_power: int) -> None:
        self.name = name
        self._health = health
        self.__max_health = health
        self.attack_power = attack_power

    @property
    def health(self) -> int:
        return self._health

    @property
    def is_alive(self) -> bool:
        return self.health > 0

    def take_damage(self, damage: int) -> None:
        if damage < 0:
            raise ValueError("Damage must be a non-negative integer.")
        self._health = max(0, self._health - damage)

    def heal(self, amount: int) -> None:
        if amount < 0:
            raise ValueError("Heal points must be a non-negative integer.")
        self._health = min(self.__max_health, self._health + amount)
        print(f"{self.name} got {amount} heal points! - Health: {self.health}")

    def attack(self, target: Character) -> None:
        if not self.is_alive:
            return
        
        target.take_damage(self.attack_power)
        print(f"{self.name} attacks {target.name} for {self.attack_power} damage!")
        
        if not target.is_alive:
            print(f"{self.name} killed {target.name}!")

    def describe(self) -> str:
        if not self.is_alive:
            return f"{self.name} - DEAD"
        return f"{self.name} - HP: {self.health} - ATK: {self.attack_power}"

            
