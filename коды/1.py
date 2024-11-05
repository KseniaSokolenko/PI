class Name:
    __slots__ = ["name"]
    def __init__(self, name):
        if name == "Ксюша":
            self.name = f"Да, я {name}"
        else:
            self.name = f"Нет, я не {name}, я Ксюша"

person1 = Name("Ксюша")
person2 = Name("София")
print(person1.name)
print(person2.name)