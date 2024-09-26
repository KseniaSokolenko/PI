# Тема 4. Функции и модули
Отчёт по теме выполнила:
  - Соколенко Ксения Алексеевна 
  - ПИЭ-22-1

| Задание | Лаб_раб | Сам_раб |
| ------ | ------ | ------ |
| Задание 1 | + | + |
| Задание 2 | + | + | 
| Задание 3 | + | + | 
| Задание 4 | + | + |
| Задание 5 | + | + | 
| Задание 6 | + | - | 
| Задание 7 | + | - | 
| Задание 8 | + | - | 
| Задание 9 | + | - | 
| Задание 10 | + | - | 

знак "+" - задание выполнено; знак "-" - задание не выполнено;

Работу проверили:
- к.э.н., доцент Панов М.А.

## Лабораторные задания:

### №1. 
Напишите функцию, которая выполняет любые арифметические действия и выводит результат в консоль. Вызовите функцию используя “точку входа”.
### Ответ:
```python
def main():
    print(2+2)

if __name__ == '__main__':
    main()
```
![Меню](https://github.com/KseniaSokolenko/PI/blob/theme_4/%D0%BA%D0%B0%D1%80%D1%82%D0%B8%D0%BD%D0%BA%D0%B8/1.png)

### Вывод: 

### №2. 
Напишите функцию, которая выполняет любые арифметические действия, возвращает при помощи return значение в место, откуда вызывали функцию. Выведите результат в консоль. Вызовите функцию используя “точку входа”.
### Ответ:
```python
def main():
    return 2+2

if __name__ == '__main__':
    print(main())
```
![Меню](https://github.com/KseniaSokolenko/PI/blob/theme_4/%D0%BA%D0%B0%D1%80%D1%82%D0%B8%D0%BD%D0%BA%D0%B8/2.1.png)

Ниже представлена точно такая же программа, как и выше, только написана более развернуто. В это программе стоит заметить что результат работы функции main() мы помещаем в переменную “answer”, в дальнейшем можно как-то работать с ним, не вызывая функцию повторно, что хорошо сказывается, например, на скорости работы программы.

```python
def main():
    result = 2+2
    return result

if __name__ == '__main__':
    answer = main()
    print(answer)
```

![Меню](https://github.com/KseniaSokolenko/PI/blob/theme_4/%D0%BA%D0%B0%D1%80%D1%82%D0%B8%D0%BD%D0%BA%D0%B8/2.2.png)

### Вывод: 

### №3. 
Напишите функцию, в которую передаются два аргумента, над ними производится арифметическое действие, результат возвращается туда, откуда эту функцию вызывали. Выведите результат в консоль. Вызовите функцию в любом небольшом цикле.

На скриншоте ниже приведен пример программы, в которой аргумент функции "x" превращается в параметр “one”, то же самое происходит "y" и “two”
### Ответ:
```python
def main(one, two):
     result = one + two
     return result

if __name__ == '__main__':
    for i in range(5):
        x =1
        y =10
        answer = main(x, y)
        print(answer)
```
![Меню](https://github.com/KseniaSokolenko/PI/blob/theme_4/%D0%BA%D0%B0%D1%80%D1%82%D0%B8%D0%BD%D0%BA%D0%B8/3.1.png)

Ниже представлена точно такая же программа, как и выше, только аргументы передаются в вызове функции, а не как отдельные переменные.

```python
def main(one, two):
     return one + two

if __name__ == '__main__':
    for i in range(5):
        answer = main(one=1, two=10)
        print(answer)
```

![Меню](https://github.com/KseniaSokolenko/PI/blob/theme_4/%D0%BA%D0%B0%D1%80%D1%82%D0%B8%D0%BD%D0%BA%D0%B8/3.2.png)

### Вывод: 

### №4. 
Напишите функцию, на вход которой подается какое-то изначальное неизвестное количество аргументов, над которыми будет производится арифметические действия. Для выполнения задания необходимо использовать кортеж “*args”. На скриншоте ниже приведен пример такой программы с комментариями.

Для закрепления понимания работы с кортежами настоятельно рекомендуем поменять аргументы вызова функции, вручную посчитать
результат, только потом запустить программу с новыми значениями и проверить себя, насколько вы поняли данный аспект программирования.
### Ответ:
```python
def main(x, *args):
    one = x
    two = sum(args)
    three = float(len(args))
    print (f"one={one}\ntwo={two}\nthree={three}")

    return x + sum(args) / float(len(args))

if __name__ == '__main__':
    result = main(11, 2, 0, 3, 10, -1, -4, 1)
    print(f"\nresult={result}")
```
![Меню](https://github.com/KseniaSokolenko/PI/blob/theme_4/%D0%BA%D0%B0%D1%80%D1%82%D0%B8%D0%BD%D0%BA%D0%B8/4.png)

### Вывод: 

### №5. 
Напишите функцию, которая на вход получает кортеж “**kwargs” и при помощи цикла выводит значения, поступившие в функцию. На скриншоте ниже указаны два варианта вызова функции с “**kwargs” и два варианта работы с данными, поступившими в эту функцию. Комментарии в коде и теоретическая часть помогут вам разобраться в этом нелегком аспекте. Вызовите функцию используя “точку входа”.
### Ответ:
```python
def main (**kwargs):
    for i in kwargs.items():
        print(i[0], i[1])

    print()

    for key in kwargs:
        print(f"{key} = {kwargs[key]}")

if __name__ == '__main__':
    main(x=[1,2,3], y=[3,3,0], z=[2,3,0], q=[3,3,0], w=[3,3,0])
    print()
    main(**{'x': [1,2,3], 'y': [3,3,0]})
```
![Меню](https://github.com/KseniaSokolenko/PI/blob/theme_4/%D0%BA%D0%B0%D1%80%D1%82%D0%B8%D0%BD%D0%BA%D0%B8/5.1.png)
![Меню](https://github.com/KseniaSokolenko/PI/blob/theme_4/%D0%BA%D0%B0%D1%80%D1%82%D0%B8%D0%BD%D0%BA%D0%B8/5.2.png)

### Вывод: 

### №6. 
Напишите две функции. Первая — получает в виде параметра “**kwargs”. Вторая считает среднее арифметическое из значений первой функции. Вызовите первую функцию используя “точку входа” и минимум 4 аргумента.
### Ответ:
```python
def main (**kwargs):
    for i, j in kwargs.items():
        print(f"{i}. Mean = {mean(j)}")

def mean(data):
    return sum(data) / float(len(data))

if __name__ == '__main__':
    main(x=[1,2,3], y=[3,3,0])
```
![Меню](https://github.com/KseniaSokolenko/PI/blob/theme_4/%D0%BA%D0%B0%D1%80%D1%82%D0%B8%D0%BD%D0%BA%D0%B8/6.png)

### Вывод: 

### №7. 
Создайте дополнительный файл.py. Напишите в нем любую функцию, которая будет что угодно выводить в консоль, но не вызывайте ее в нем. Откройте файл main.py, импортируйте в него функцию из нового файла и при помощи “точки входа” вызовите эту функцию.
### Ответ:
```python
def say_hello():
    print('Hello students!')
```

```python
from for_import7 import say_hello

if __name__ == '__main__':
    say_hello()
```
![Меню](https://github.com/KseniaSokolenko/PI/blob/theme_4/%D0%BA%D0%B0%D1%80%D1%82%D0%B8%D0%BD%D0%BA%D0%B8/7.1.png)
![Меню](https://github.com/KseniaSokolenko/PI/blob/theme_4/%D0%BA%D0%B0%D1%80%D1%82%D0%B8%D0%BD%D0%BA%D0%B8/7.2.png)

### Вывод: 

### №8. 
Напишите программу, которая будет выводить корень, синус, косинус полученного от пользователя числа.
### Ответ:
```python
import math

def main():
    value = int(input('Введите значение: '))
    print(math.sqrt(value))
    print(math.sin(value))
    print(math.cos(value))

if __name__ == '__main__':
    main()
```
![Меню](https://github.com/KseniaSokolenko/PI/blob/theme_4/%D0%BA%D0%B0%D1%80%D1%82%D0%B8%D0%BD%D0%BA%D0%B8/8.1.png)

На первом скриншоте мы просто импортировали модуль таш целиком и вызвали его длинным способом через math.название_фунции. Также импорт стандартного модуля в python возможно осуществить и другими способами, которые будут выполнять ту же самую функцию, но синтаксис будет немного отличатся.
На втором скриншоте из модуля math мы загрузили в программу только 3 необходимые функции и обращались к ним так, будто они находятся у нас в файле просто через их название. Также замечу что мы импортировали три функции в одну строку. что очень удобно.

```python
from math import sqrt, sin, cos

def main():
    value = int(input('Введите значение: '))
    print(sqrt(value))
    print(sin(value))
    print(cos(value))

if __name__ == '__main__':
    main()
```

![Меню](https://github.com/KseniaSokolenko/PI/blob/theme_4/%D0%BA%D0%B0%D1%80%D1%82%D0%B8%D0%BD%D0%BA%D0%B8/8.2.png)

На третьем скриншоте мы импортировали модуль math и при помощи оператора * загрузили все его функции. По большому счету мы сделали то же самое что и на первом скриншоте, но у нас только поменялся синтаксис вызова этих функций, он стал похож на вызов со второго скриншота.

```python
from math import *

def main():
    value = int(input('Введите значение: '))
    print(sqrt(value))
    print(sin(value))
    print(cos(value))

if __name__ == '__main__':
    main()
```

![Меню](https://github.com/KseniaSokolenko/PI/blob/theme_4/%D0%BA%D0%B0%D1%80%D1%82%D0%B8%D0%BD%D0%BA%D0%B8/8.3.png)

### Вывод: 

### №9. 
Напишите программу, которая будет рассчитывать какой день недели будет через n-нное количество дней, которые укажет пользователь.
### Ответ:
```python
from datetime import datetime as dt
from datetime import timedelta as td

def main():
    print(
        f"Сегодня {dt.today().date()}. "
        f"День недели - {dt.today().isoweekday()}"
    )
    n = int(input('Введите количество дней: '))
    today = dt.today()
    result = today + td(days = n)
    print(
        f"Через {n} дней будет {result.date()}. "
        f"День недели - {result.isoweekday()}"
    )

if __name__ == '__main__':
    main()
```
![Меню](https://github.com/KseniaSokolenko/PI/blob/theme_4/%D0%BA%D0%B0%D1%80%D1%82%D0%B8%D0%BD%D0%BA%D0%B8/9.png)

В результате день недели указан в виде цифры, где 1 = понедельник, 2 = вторник, 3 = среда и так далее.

### Вывод: 

### №10. 
Напишите программу с использованием глобальных переменных, которая будет считать площадь треугольника или прямоугольника в зависимости от того, что выберет пользователь. Получение всей необходимой информации реализовать через input(), а подсчет площадей выполнить при помощи функций. Результатом программы будет число, равное площади, необходимой фигуры.
### Ответ:
```python
global result

def rectangle():
    a = float(input("Ширина = "))
    b = float(input("Высота = "))
    global result
    result = a*b

def triangle():
    a = float(input("Основание = "))
    h = float(input("Высота = "))
    global result
    result = 0.5*a*h

figure = input("1-й прямоугольник, 2-й треугольник: ")

if __name__ == '__main__':
    if figure == '1':
        rectangle()
    elif figure == '2':
        triangle()

print(f"Площадь: {result}")
)
```
![Меню](https://github.com/KseniaSokolenko/PI/blob/theme_4/%D0%BA%D0%B0%D1%80%D1%82%D0%B8%D0%BD%D0%BA%D0%B8/10.1.png)
![Меню](https://github.com/KseniaSokolenko/PI/blob/theme_4/%D0%BA%D0%B0%D1%80%D1%82%D0%B8%D0%BD%D0%BA%D0%B8/10.2.png)

### Вывод: 

## Самостоятельные задания:

### №1. 
Дайте подробный комментарий для кода, написанного ниже. Комментарий нужен для каждой строчки кода, нужно описать что она делает. Не забудьте, что функции комментируются по-особенному.

```python
from datetime import datetime
from math import sqrt

def main(**kwargs):
 for key in kwargs.items():
  result = sqrt(key[1][O] ** 2 + key[1][1] ** 2)
  print(result)

if __name__ == '__main__'
 start_time = datetime.now()
 main(
 one=[10, 3],
 two=[5, 4],
 three=[15, 13],
 four=[93, 53],
 five=[133, 15]
 )

time_costs = datetime.now() - start_time

print(f"Время выполнения программы - {time_costs}")
```

### Ответ:
```python
from datetime import datetime # Импортируем модуль для работы с датами и временем
from math import sqrt # Импортируем модуль для вычисления квадратного корня

def main(**kwargs):
    """ Определяем функцию main, принимающую параметры через словарь kwargs
    """
    for key in kwargs.items(): # Перебираем все ключи и значения в словаре kwargs
        # Задаем точки x1,x2 и y1,y2
        x1 = key[1][0]
        y1 = key[1][1]
        x2 = x1
        y2 = y1
        distance = sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2) # Вычисляем расстояние между двумя точками
        print(distance) # Печатаем расстояние

if __name__ == '__main__': # Запускаем программу только если она используется как основной скрипт
    start_time = datetime.now() # Начальное время выполнения программы
    main( # Вызываем функцию main с конкретными параметрами
        one=[10, 3],
        two=[5, 4],
        three=[15, 13],
        four=[93, 53],
        five=[133, 15]
    )
    time_costs = datetime.now() - start_time  # Время выполнения программы
    print(f"Время выполнения программы - {time_costs}") # Печатаем время выполнения программы
```
![Меню](https://github.com/KseniaSokolenko/PI/blob/theme_4/%D0%BA%D0%B0%D1%80%D1%82%D0%B8%D0%BD%D0%BA%D0%B8/s1.1.png)
![Меню](https://github.com/KseniaSokolenko/PI/blob/theme_4/%D0%BA%D0%B0%D1%80%D1%82%D0%B8%D0%BD%D0%BA%D0%B8/s1.2.png)

### Вывод: 

### №2. 
Напишите программу, которая будет заменять игральную кость с 6 гранями. Если значение равно 5 или 6, то в консоль выводится «Вы победили», если значения 3 или 4, то вы рекурсивно должны вызвать эту же функцию, если значение 1 или 2, то в консоль выводится «Вы проиграли». При этом каждый вызов функции необходимо выводить в консоль значение “кубика”. Для выполнения задания необходимо использовать стандартную библиотеку random. Программу нужно написать, используя одну функцию и “точку входа”
### Ответ:
```python
import random

def roll_dice():
    dice_value = random.randint(1, 6)

    if dice_value in [5, 6]:
        print("Вы победили")
    elif dice_value in [3, 4]:
        return roll_dice()
    else:
        print("Вы проиграли")

    print("Значение на кубике: ", dice_value)

if __name__ == '__main__':
    roll_dice()
```
![Меню](https://github.com/KseniaSokolenko/PI/blob/theme_4/%D0%BA%D0%B0%D1%80%D1%82%D0%B8%D0%BD%D0%BA%D0%B8/s2.png)

### Вывод: 

### №3. 
Напишите программу, которая будет выводить текущее время, с точностью до секунд на протяжении 5 секунд. Программу нужно написать с использованием цикла. Подсказка: необходимо использовать модуль datetime и date, а также вам необходимо как-то “усыплять” программу на 1 секунду.
### Ответ:
```python
def main():
    import datetime
    from time import sleep

    current_time = datetime.datetime.now().strftime("%H:%M:%S")

    for _ in range(5):
        print(current_time)
        sleep(1)
        current_time = datetime.datetime.now().strftime("%H:%M:%S")

if __name__ == '__main__':
    main()
```
![Меню](https://github.com/KseniaSokolenko/PI/blob/theme_4/%D0%BA%D0%B0%D1%80%D1%82%D0%B8%D0%BD%D0%BA%D0%B8/s3.png)

### Вывод: 

### №4. 
Напишите программу, которая считает среднее арифметическое от аргументов вызываемой функции, с условием того, что изначальное количество этих аргументов неизвестно. Программу необходимо реализовать используя одну функцию и “точку входа”.
### Ответ:
```python
def calculate_average(args):
    total = sum(args)
    return total / len(args)

if __name__ == '__main__':
    args = list(map(float, input('Введите значения: ').split()))
    average = calculate_average(args)
    print(f'Среднее арифметическое: {average}')
```
![Меню](https://github.com/KseniaSokolenko/PI/blob/theme_4/%D0%BA%D0%B0%D1%80%D1%82%D0%B8%D0%BD%D0%BA%D0%B8/s4.png)

### Вывод: 

### №5. 
Создайте два Python файла, в одном будет выполняться вычисление площади треугольника при помощи формулы Герона (необходимо реализовать через функцию), а во втором будет происходить взаимодействие с пользователем (получение всей необходимой информации и вывод результатов). Напишите эту программу и выведите в консоль полученную площадь.
### Ответ:
```python
import math

def heron(a, b, c):
    s = (a + b + c) / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    return area
```
![Меню](https://github.com/KseniaSokolenko/PI/blob/theme_4/%D0%BA%D0%B0%D1%80%D1%82%D0%B8%D0%BD%D0%BA%D0%B8/s5.2.png)

```python
from s5_TRIANGLE import heron

a = float(input("Введите первую сторону треугольника: "))
b = float(input("Введите вторую сторону треугольника: "))
c = float(input("Введите третью сторону треугольника: "))

area = heron(a, b, c)
if __name__ == '__main__':
    print(f"Площадь треугольника равна {area}")
```
![Меню](https://github.com/KseniaSokolenko/PI/blob/theme_4/%D0%BA%D0%B0%D1%80%D1%82%D0%B8%D0%BD%D0%BA%D0%B8/s5.1.png)

### Вывод: 

## Общий вывод по теме:
