class Tomato:
    # Словарь состояний, описывающий этапы созревания
    states = {0: 'Отсутствует', 1: 'Цветение', 2: 'Зеленый', 3: 'Красный'}

    def __init__(self, index):
        """
        Инициализация объекта Tomato.
        Параметры:
        index (int): Индекс томата для идентификации.
        state (int): Текущее состояние томата.
        """
        self._index = index
        self._state = 0

    def grow(self):
        """
        Метод для перехода на следующую стадию.
        Увеличивает текущее состояние на 1.
        """
        self._state = self._state + 1

    def is_ripe(self):
        """
        Проверяем, достиг ли томат стадии зрелости.
        Возвращаетbool: True, если томат созрел (стадия 3), иначе False.
        """
        return self._state == 3


class TomatoBush:
    def __init__(self, tomato_num):
        """
        Инициализация объекта TomatoBush.
        Параметры:
        tomato_num (int): Количество томатов на кусте.
        tomatoes (list): Список объектов Tomato, представляющих томаты на кусте.
        """
        self.tomatoes = [Tomato(index) for index in range(0, tomato_num)]

    def grow_all(self):
        """
        Переводит все томаты на следующую стадию.
        """
        for tomato in self.tomatoes:
            tomato.grow()

    def all_are_ripe(self):
        """
        Проверяет, все ли томаты на кусте созрели.
        Возвращает:
        bool: True, если все томаты достигли стадии зрелости, иначе False.
        """
        return all(tomato.is_ripe() for tomato in self.tomatoes)

    def give_away_all(self):
        """
        Удаляет все томаты с куста.
        """
        self.tomatoes = []


class Gardener:
    def __init__(self, name, plant):
        """
        Инициализация объекта Gardener.

        Параметры:
        name (str): Имя садовника.
        plant (TomatoBush): Куст томатов, за которым ухаживает садовник.
        """
        self.name = name
        self._plant = plant

    def work(self):
        """
        Уход за кустом: переводит все томаты куста на следующую стадию созревания.
        """
        self._plant.grow_all()
        print("Ухаживаем за растениями")

    def harvest(self):
        """
        Сбор урожая, если все томаты на кусте созрели.

        Если все томаты достигли стадии зрелости, урожай собирается,
        и все томаты удаляются с куста. Если не все томаты созрели,
        выводится соответствующее сообщение.
        """
        if self._plant.all_are_ripe():
            self._plant.give_away_all()
            print('Урожай собран')
        else:
            print('Томаты еще не созрели')

    @staticmethod
    def knowledge_base():
        """
        Вывод информации о порядке действий для ухода за кустом томатов.
        """
        print("Справка по садоводству: ")
        print("1. Посадить куст томатов")
        print("2. Назначить садовника на куст")
        print("3. Ухаживать за кустом")
        print("4. Собрать урожай")


# Вызов справки
# Gardener.knowledge_base()
# Создание куста с четырьмя томатами
bush = TomatoBush(4)
# Создание садовника и назначение его на куст томатов
gardener = Gardener('Ксюша', bush)

# Уход за кустом
gardener.work()
