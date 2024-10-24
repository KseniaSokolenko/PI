class Animals:
    def sound(self):
        pass
    def get_name(self):
        pass

class Cow(Animals):
    def __init__(self, name):
        self.name = name
    def get_name(self):
        return self.name
    def sound(self):
        print("Му-му")

class Cat(Animals):
    def __init__(self, name):
        self.name = name
    def get_name(self):
        return self.name
    def sound(self):
        print("Мяу-мяу")

class Dog(Animals):
    def __init__(self, name):
        self.name = name
    def get_name(self):
        return self.name
    def sound(self):
        print("Гав-гав")

animals = [Cow('Зорька'), Cat('Барсик'), Dog('Жучка')]

for animal in animals:
    print(f"Имя животного: {animal.get_name()}")
    animal.sound()