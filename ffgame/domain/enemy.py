from domain.character import Character
import random

class Reno(Character):
    def __init__(self):
        super().__init__("Reno", 160, 14, 20)

    def perform_action(self, target):
        action_type = random.choice(["basic", "electric"])  # Decide ataque

        if action_type == "basic":
            damage = self._attack + random.randint(0, 4)
            target.take_damage(damage)
            return f"{self._name} golpea con su bastón ({damage} daño)."

        else:
            if self._mp >= 5:  # Usa MP
                self._mp -= 5
                damage = 22
                target.take_damage(damage)
                return f"{self._name} usa Electro Shock ({damage} daño)."
            else:
                damage = self._attack
                target.take_damage(damage)
                return f"{self._name} ataca (sin MP) ({damage} daño)."