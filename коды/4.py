class Mammal:
    className = "Mammal"

class Dog(Mammal):
    species = "canine"
    sounds = "wow"
    meeting = "wags his tail"

class Cat(Mammal):
    species = "feline"
    sounds = "meow"
    meeting = "rubs against your legs"

dog = Dog()
print(f"Dog is {dog.className}, but it says {dog.sounds}. During a meeting, it {dog.meeting}.")
cat = Cat()
print(f"Cat is {cat.className}, but it says {cat.sounds}. During a meeting, it {cat.meeting}.")