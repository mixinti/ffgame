from domain.heroes import Cloud, Aerith, Tifa
from domain.enemy import Reno
from ui.console import ConsoleUI
import random

class Game:
    def __init__(self):
        self.ui = ConsoleUI()

        # Crear personajes
        self.cloud = Cloud()
        self.tifa = Tifa()
        self.aerith = Aerith()
        self.enemy = Reno()

        # Orden de turnos intercalado
        self.turn_order = [
            self.cloud,
            self.enemy,
            self.tifa,
            self.enemy,
            self.aerith,
            self.enemy
        ]

    def run(self):
        self.ui.show_message("Pelea contra Reno")

        # Loop principal
        while self.enemy.is_alive() and any(h.is_alive() for h in [self.cloud, self.tifa, self.aerith]):
            for actor in self.turn_order:

                # Si el enemigo muere, cortar
                if not self.enemy.is_alive():
                    break

                # Si el actor es héroe y está muerto, saltear
                if actor != self.enemy and not actor.is_alive():
                    continue

                # Ejecutar turno
                self.execute_turn(actor)

        self.end_game()

    def execute_turn(self, actor):
        # Turno del enemigo
        if actor == self.enemy:
            self.enemy_turn()
            return

        # Turno del jugador
        self.ui.show_status(actor, self.enemy)
        choice = self.ui.choose_action(actor)

        if choice == "1":
            log = actor.perform_action(self.enemy)

        elif choice == "2" and actor.skill:
            log = actor.skill.use(actor, self.enemy)

        elif choice == "3" and actor.spells:
            log = self.cast_spell(actor)

        else:
            log = "Acción inválida."

        self.ui.show_message(log)

    def cast_spell(self, hero):
        spell = self.ui.choose_spell(hero)

        if spell is None:
            return "Cancelado."

        if spell.__class__.__name__ == "Cure":
            target = self.ui.choose_ally([self.cloud, self.tifa, self.aerith])
        else:
            target = self.enemy

        return spell.cast(hero, target)

    def enemy_turn(self):
        heroes_alive = [h for h in [self.cloud, self.tifa, self.aerith] if h.is_alive()]
        target = random.choice(heroes_alive)
        log = self.enemy.perform_action(target)
        self.ui.show_message(f"\n[Enemigo] {log}")

    def end_game(self):
        if self.enemy.is_alive():
            self.ui.show_message("Derrota...")
        else:
            self.ui.show_message("Victoria!")