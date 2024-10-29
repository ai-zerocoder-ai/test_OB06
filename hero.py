class Hero:
    def __init__(self, name: str, health: int = 100, attack_power: int = 20):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def attack(self, other: 'Hero'):
        other.receive_damage(self.attack_power)
        print(f"{self.name} атаковал {other.name} на {self.attack_power} урона.")

    def receive_damage(self, damage: int):
        self.health -= damage
        if self.health < 0:
            self.health = 0

    def is_alive(self) -> bool:
        return self.health > 0

    def __str__(self):
        return f"{self.name}: Здоровье = {self.health}, Сила атаки = {self.attack_power}"
