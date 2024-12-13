from weapon import fists
from health_bar import Healthbar

class character:

    def __init__(self, 
                 name: str, 
                 health: int, 
                 damage: int,
                 ) -> None:
        self.name = name
        self.health = health
        self.health_max = health
        self.damage = damage

        self.weapon = fists

def attack(self, target) -> None:
    target.health -= self.weapon.damage
    target.health = max(target.health, 0)
    target.health_bar.update()
    print(f"{self.name} dealt {self.weapon.damage} damage to {target.name} with {self.weapon.name}")


class Hero(character):
    def __init__(self, 
                 name: str, 
                 health: int) -> None:
        super().__init__(name=name, health=health)

        self.default_weapon = self.weapon
        self.health_bar = Healthbar(self, color="green")

    def equip(self, weapon) -> None:
        self.weapon = weapon
        print(f"{self.name} equipped a(n) {self.weapon.name} !")

    def drop(self) -> None:
        print(f"{self.name} droppen the {self.weapon}!")
        self.weapon = self.default_weapon


class Enemy(character):
    def __init__(self, 
                 name: str, 
                 health: int,
                 weapon,
                 ) -> None:
        super().__init__(name=name, health=health)
        self.weapon =weapon

        self.health_bar = Healthbar(self, color="red")
