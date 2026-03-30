from domain.heroes import Cloud, Aerith, Tifa

from domain.enemy import Reno

# Importamos la interfaz de consola (para mostrar texto y pedir input)
from ui.console import ConsoleUI

# Importamos la librería random para decisiones aleatorias
import random

# Definimos la clase Game (el motor del juego)
class Game:

    # Constructor: se ejecuta automáticamente al crear Game()
    def __init__(self):
        # Creamos la interfaz de usuario
        self.ui = ConsoleUI()

        # Creamos los personajes (objetos)
        self.cloud = Cloud()
        self.tifa = Tifa()
        self.aerith = Aerith()

        # Creamos el enemigo
        self.enemy = Reno()

        # Definimos el orden de turnos (lista)
        self.turn_order = [
            self.cloud,   # turno de Cloud
            self.enemy,   # turno de Reno
            self.tifa,    # turno de Tifa
            self.enemy,   # turno de Reno
            self.aerith,  # turno de Aerith
            self.enemy    # turno de Reno
        ]

    # Método principal del juego
    def run(self):
        # Mostramos mensaje inicial
        self.ui.show_message("Reno Fight")

        # Loop principal del juego
        # Se ejecuta mientras:
        # - el enemigo esté vivo
        # - al menos un héroe esté vivo
        while self.enemy.is_alive() and any(h.is_alive() for h in [self.cloud, self.tifa, self.aerith]):

            # Recorremos el orden de turnos
            for actor in self.turn_order:

                # Si el enemigo murió, salimos del loop
                if not self.enemy.is_alive():
                    break

                # Si el actor es un héroe y está muerto, lo saltamos
                if actor != self.enemy and not actor.is_alive():
                    continue

                # Ejecutamos el turno del actor
                self.execute_turn(actor)

        # Cuando termina el loop, mostramos resultado final
        self.end_game()

    # Ejecuta el turno de un personaje
    def execute_turn(self, actor):

        # Si el actor es el enemigo
        if actor == self.enemy:
            # Ejecutamos turno enemigo
            self.enemy_turn()
            return  # terminamos función

        # Mostramos estado del personaje y enemigo
        self.ui.show_status(actor, self.enemy)

        # Pedimos acción al jugador
        choice = self.ui.choose_action(actor)

        # Si elige ataque básico
        if choice == "1":
            log = actor.perform_action(self.enemy)

        # Si elige habilidad y tiene una
        elif choice == "2" and actor.skill:
            log = actor.skill.use(actor, self.enemy)

        # Si elige magia y tiene hechizos
        elif choice == "3" and actor.spells:
            log = self.cast_spell(actor)

        # Si no eligió algo válido
        else:
            log = "Acción inválida."

        # Mostramos resultado
        self.ui.show_message(log)

    # Maneja lanzamiento de hechizos
    def cast_spell(self, hero):

        # Usuario elige hechizo
        spell = self.ui.choose_spell(hero)

        # Si no eligió nada válido
        if spell is None:
            return "Cancelado."

        # Si el hechizo es de curación
        if spell.__class__.__name__ == "Cure":
            # Elegimos aliado
            target = self.ui.choose_ally([self.cloud, self.tifa, self.aerith])
        else:
            # Si no, objetivo es el enemigo
            target = self.enemy

        # Ejecutamos hechizo
        return spell.cast(hero, target)

    # Turno del enemigo
    def enemy_turn(self):

        # Lista de héroes vivos
        heroes_alive = [h for h in [self.cloud, self.tifa, self.aerith] if h.is_alive()]

        # Elegimos uno al azar
        target = random.choice(heroes_alive)

        # Ejecutamos acción del enemigo
        log = self.enemy.perform_action(target)

        # Mostramos resultado
        self.ui.show_message(f"\n[Enemigo] {log}")

    # Final del juego
    def end_game(self):

        # Si el enemigo sigue vivo → perdiste
        if self.enemy.is_alive():
            self.ui.show_message("Derrota...")

        # Si no → ganaste
        else:
            self.ui.show_message("Victoria!")