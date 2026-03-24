from abc import ABC, abstractmethod  # Importamos herramientas para clases abstractas

class Character(ABC):  # Clase base abstracta (NO se puede instanciar directamente)
    def __init__(self, name, hp, attack, mp):
        self._name = name      # Nombre del personaje (encapsulado)
        self._hp = hp          # Vida actual
        self._attack = attack  # Ataque base
        self._mp = mp          # Mana (para magia)

    @abstractmethod
    def perform_action(self, target):
        pass  # Método obligatorio que las clases hijas deben implementar

    def take_damage(self, amount):
        self._hp -= amount  # Reduce la vida
        if self._hp < 0:    # Evita valores negativos
            self._hp = 0

    def heal(self, amount):
        self._hp += amount  # Cura al personaje

    def use_mana(self, amount):
        if self._mp >= amount:  # Verifica si hay suficiente MP
            self._mp -= amount  # Resta el MP
            return True         # Indica que se pudo usar
        return False            # No había suficiente MP

    def is_alive(self):
        return self._hp > 0  # Retorna True si sigue vivo

    @property
    def name(self):
        return self._name  # Getter (encapsulamiento)

    @property
    def hp(self):
        return self._hp

    @property
    def mp(self):
        return self._mp