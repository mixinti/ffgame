from domain.character import Character
from domain.skills import HeavySlash, ComboKick
from domain.spells import Fire, Cure

class Cloud(Character):
    def __init__(self):
        super().__init__("Cloud", 120, 18, 30)  # Stats base
        self.skill = HeavySlash()               # Habilidad única
        self.spells = [Fire()]                  # Lista de hechizos

    def perform_action(self, target):
        damage = self._attack
        target.take_damage(damage)
        return f"{self._name} ataca ({damage} daño)."

class Aerith(Character):
    def __init__(self):
        super().__init__("Aerith", 90, 10, 60)
        self.skill = None                       # No tiene skill física
        self.spells = [Cure(), Fire()]          # Soporte + ataque

    def perform_action(self, target):
        damage = self._attack
        target.take_damage(damage)
        return f"{self._name} golpea ({damage} daño)."

class Tifa(Character):
    def __init__(self):
        super().__init__("Tifa", 100, 12, 20)
        self.skill = ComboKick()
        self.spells = []                        # No usa magia

    def perform_action(self, target):
        damage = self._attack
        target.take_damage(damage)
        return f"{self._name} golpea ({damage} daño)."