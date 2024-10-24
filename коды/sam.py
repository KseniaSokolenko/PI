class Animal:
    def __init__(self, name, klass):
        self._name = name
        self.__klass = klass

    def place(self):
        a = input(f'Введите, где обитает {self._name}:')
        print(f"Верно, {self._name} принадлежит классу {self.__klass} и обитает", a)

an_animal = Animal("кузнечик", "насекомое")
print(an_animal._name)
an_animal.place()

