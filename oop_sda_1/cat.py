# class Cat:
#     def __init__(self, name: str, sound="meow"):
#         self.name = name
#         self.sound = sound
#
#     def make_sound(self) -> str:
#         return f'Name is {self.name} sound is meow'

from oop_sda_1.animal import Animal
from oop_sda_1.moveable import Movable

class Cat(Movable, Animal):

    def __init__(self, name: str, sound: str = 'Meow', eaten_mauses: int = 0):
        super().__init__(self, name, sound)
        self.eaten_mauses = eaten_mauses

    def make_sound(self) -> str:
        return f"{self.name} makes {self.sound}"

    def eat_mouse(self) -> None:
        self.eaten_mauses += 1

    def count_eaten_mouses(self) -> int:
        print(f'{self.name} ate {self.eaten_mauses} mauses.')
        return self.eaten_mauses

    def move(self) -> str:
        return f'Chodzę po dachach.'