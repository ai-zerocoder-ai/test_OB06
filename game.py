from hero import Hero


class Game:
    def __init__(self, player: Hero, computer: Hero):
        self.player = player
        self.computer = computer

    def start(self):
        print("=== Битва героев начинается! ===")
        print(self.player)
        print(self.computer)
        print("-------------------------------")

        turn = 0  # 0 - игрок, 1 - компьютер

        while self.player.is_alive() and self.computer.is_alive():
            if turn == 0:
                attacker = self.player
                defender = self.computer
            else:
                attacker = self.computer
                defender = self.player

            attacker.attack(defender)
            print(f"{defender.name} осталось здоровья: {defender.health}")
            print("-------------------------------")

            turn = 1 - turn  # переключение хода

        self.declare_winner()

    def declare_winner(self):
        if self.player.is_alive():
            print(f"Победитель: {self.player.name}!")
        else:
            print(f"Победитель: {self.computer.name}!")


if __name__ == "__main__":
    player_name = input("Введите имя вашего героя: ")
    player = Hero(name=player_name)
    computer = Hero(name="Компьютер")
    game = Game(player, computer)
    game.start()
