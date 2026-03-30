class ConsoleUI:

    # Muestra mensaje
    def show_message(self, message):
        print(message)

    # Muestra estado
    def show_status(self, hero, enemy):
        print(f"\n{hero.name} HP: {hero.hp} | MP: {hero.mp} | Enemy HP: {enemy.hp}")

    # Elegir acción
    def choose_action(self, hero):
        print(f"\nTurno de {hero.name}")
        print("1. Ataque")

        if hero.skill:
            print("2. Habilidad")

        if hero.spells:
            print("3. Magia")

        return input("Elegí acción: ")

    # Elegir hechizo
    def choose_spell(self, hero):
        print("\nHechizos:")

        for i, spell in enumerate(hero.spells):
            print(f"{i+1}. {spell.__class__.__name__} (Costo: {spell.cost})")

        choice = input("Elegí hechizo: ")

        if not choice.isdigit():
            return None

        idx = int(choice) - 1

        if 0 <= idx < len(hero.spells):
            return hero.spells[idx]

        return None

    # Elegir aliado
    def choose_ally(self, heroes):
        alive = [h for h in heroes if h.is_alive()]

        print("\nElegí objetivo:")

        for i, h in enumerate(alive):
            print(f"{i+1}. {h.name} (HP: {h.hp})")

        choice = input("Target: ")

        if not choice.isdigit():
            return alive[0]

        idx = int(choice) - 1

        return alive[idx] if 0 <= idx < len(alive) else alive[0]