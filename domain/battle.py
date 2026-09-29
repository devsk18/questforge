

from domain.character import Character


def run_special_round(attacker: Character, defender: Character) -> None:
    attacker.special_ability(defender)

def total_party_damage(party: list[Character], target: Character) -> None:
    for member in party:
        if member.is_alive and target.is_alive:
            member.attack(target)