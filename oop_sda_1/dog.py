class Dog:
    def __init__(self, name: str, sound: str):
        self.name = name
        self.sound = sound

    def make_sound(self) -> str:
        return f'Pies wydaje dźwięk {self.sound} i ma na imię {self.name}'