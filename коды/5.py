# Определение базового класса для геометрических фигур
class Shape:
    # Абстрактный метод для вычисления площади фигуры
    def area(self):
        pass

# Класс прямоугольника, наследующий от класса Shape
class Rectangle(Shape):
    # Конструктор класса, принимающий ширину и высоту прямоугольника
    def __init__(self, width, height):
        # Сохранение ширины и высоты в экземпляре класса
        self.width = width
        self.height = height

    # Метод для вычисления площади прямоугольника
    def area(self):
        # Возвращает произведение ширины и высоты
        return self.width * self.height

# Класс круга, также наследующий от класса Shape
class Circle(Shape):
    # Конструктор класса, принимающий радиус круга
    def __init__(self, radius):
        # Сохранение радиуса в экземпляре класса
        self.radius = radius

    # Метод для вычисления площади круга
    def area(self):
        # Возвращает площадь круга по формуле π * r^2
        return 3.14 * self.radius ** 2

# Создание списка объектов фигур (прямоугольник и круг)
shapes = [Rectangle(4, 5), Circle(5)]

# Проход по всем фигурам в списке и вывод их площадей
for shape in shapes:
    # Вывод строки с площадью текущей фигуры
    print(f"Площадь: {shape.area()}")