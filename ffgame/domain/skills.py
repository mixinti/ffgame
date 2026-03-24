from abc import ABC, abstractmethod

class Skill(ABC):  # Clase abstracta de habilidades
    @abstractmethod
    def use(self, user, target):
        pass  # Cada skill define su comportamiento

class HeavySlash(Skill):
    def use(self, user, target):
        damage = user._attack * 2  # Daño fuerte (x2)
        target.take_damage(damage) # Aplica daño
        return f"{user.name} usa Heavy Slash ({damage} daño)."

class ComboKick(Skill):
    def use(self, user, target):
        total = 0  # Acumula daño total
        for _ in range(3):  # 3 golpes
            dmg = user._attack // 2  # Cada golpe es más débil
            target.take_damage(dmg)
            total += dmg
        return f"{user.name} usa Combo Kick ({total} daño total)."