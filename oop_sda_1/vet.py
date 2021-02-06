from oop_sda_1.animal import Animal
from oop_sda_1.cat import Cat
from oop_sda_1.dog import Dog


class Vet:

    @classmethod
    def say_cat_hello(cls, cat: Cat) -> str:
        return f'Hello, little {cat.name}!'

    @classmethod
    def say_dog_hello(cls, dog: Dog) -> str:
        return f'Hello, brave {dog.name}!'

    @classmethod
    def say_hello(cls, animal: Animal) -> str:
        return f'Hello, {animal.name}'