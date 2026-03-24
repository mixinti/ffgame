from abc import ABC, abstractmethod

class Spell(ABC):
    def __init__(self, cost):
        self.cost = cost  # Costo de MP del hechizo

    @abstractmethod
    def cast(self, caster, target):
        pass

class Fire(Spell):
    def __init__(self):
        super().__init__(10)  # Costo 10 MP

    def cast(self, caster, target):
        if not caster.use_mana(self.cost):  # Verifica MP
            return "MP insuficiente."
        damage = 25
        target.take_damage(damage)
        return f"{caster.name} lanza Fire ({damage} daño)."

class Ice(Spell):
    def __init__(self):
        super().__init__(8)

    def cast(self, caster, target):
        if not caster.use_mana(self.cost):
            return "MP insuficiente."
        damage = 20
        target.take_damage(damage)
        return f"{caster.name} lanza Ice ({damage} daño)."

class Cure(Spell):
    def __init__(self):
        super().__init__(12)

    def cast(self, caster, target):
        if not caster.use_mana(self.cost):
            return "MP insuficiente."
        heal = 30
        target.heal(heal)
        return f"{caster.name} lanza Cure y cura {heal} HP a {target.name}."