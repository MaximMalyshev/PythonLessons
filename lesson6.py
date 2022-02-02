from itertools import cycle
from time import sleep


class TrafficLight:
    colors = ("Красный", "Желтый", "Зеленый")
    times = (7, 2, 4)

    def __init__(self, color):
        self.__color = color

    def running(self):
        colors_cycle = cycle(self.colors)
        for color in colors_cycle:
            if self.__color == color:
                print(self.__color)
                sleep(self.times[self.colors.index(self.__color)])
                self.__color = next(colors_cycle)


class Road:
    wsm = 25  # вес 1 кв.м асфальта толщиной 1см в кг

    def __init__(self, width, length):
        self._width = width
        self._length = length

    def weight(self, height_sm):  # возвращает вес в кг
        return self._width * self._length * self.wsm * height_sm


class Worker:
    _validated = False

    def __init__(self, name, surname, position, income):
        if len(name) == 0:
            print("Ошибка! Имя - обязательный параметр")
            return
        if len(surname) == 0:
            print("Ошибка! Фамилия - обязательный параметр")
            return
        if len(position) == 0:
            print("Ошибка! Должность - обязательный параметр")
            return
        self.name = name
        self.surname = surname
        self.position = position
        try:
            self._income = income
            if income['wage'] <= 0:
                print("Ошибка! Оклад должен быть > 0")
                return
            if income['bonus'] <= 0:
                print("Ошибка! Премия должна быть > 0")
                return
            self._validated = True
        except KeyError:
            print("Ошибка! Неверный формат данных атрибута income. "
                  "Используйте данные в виде {'wage': wage, 'bonus': bonus}")


class Position(Worker):
    def get_full_name(self):
        if self._validated:
            return f"{self.name} {self.surname}"
        else:
            print('Данные сотрудника не корректны')

    def get_total_income(self):
        if self._validated:
            return self._income['wage'] + self._income['bonus']
        else:
            print('Данные сотрудника не корректны')


class Car:
    direction = "Не определено"
    state = "Стоит"

    def __init__(self, direction, speed, color, name, is_police):
        self.direction = direction
        self.speed = speed
        if speed != 0:
           self.state = "Движется"
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self, speed):
        self.speed = speed
        if speed < 1200:
            self.state = "Движется"
        else:
            self.state = "Летит"
        self.info()

    def stop(self):
        self.state = "Стоит"
        self.speed = 0
        self.info()

    def turn(self, direction):
        self.direction = direction

    def show_speed(self):
        print(f"Скорость = {self.speed} км/ч")
        direction = "Не определено"

    def info(self):
        print(f"Авто цвета \"{self.color}\", марка \"{self.name}\" состояние \"{self.state}\" "
              f"скорость {self.speed}км/ч направление \"{self.direction}\"")


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print("Превышение скорости!")
        else:
            super().show_speed()


class SportCar(Car):
    def __init__(self, direction, speed, color, name):
        super().__init__(direction, speed, color, name, is_police=False)


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print("Превышение скорости!")
        else:
            super().show_speed()


class PoliceCar(Car):
    def __init__(self, direction, speed, color, name):
        super().__init__(direction, speed, color, name, is_police=True)


class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print("Запуск отрисовки")


class Pen(Stationery):
    def draw(self):
        print(f"Выбран {self.title}")
        super().draw()


class Pencil(Stationery):
    def draw(self):
        print(f"Выбран {self.title}")
        super().draw()


class Handle(Stationery):
    def draw(self):
        print(f"Выбран {self.title}")
        super().draw()

def run():
    print("Практическое задание 6 ----------")

    """1. Создать класс TrafficLight (светофор). определить у него один атрибут color (цвет) и метод running (запуск);
    атрибут реализовать как приватный; в рамках метода реализовать переключение светофора в режимы: красный, жёлтый,
    зелёный; продолжительность первого состояния (красный) составляет 7 секунд, второго (жёлтый) — 2 секунды,
    третьего (зелёный) — на ваше усмотрение; переключение между режимами должно осуществляться только в указанном порядке
    (красный, жёлтый, зелёный); проверить работу примера, создав экземпляр и вызвав описанный метод.
    Задачу можно усложнить, реализовав проверку порядка режимов. При его нарушении выводить соответствующее сообщение и
    завершатьскрипт. """

    traffic = TrafficLight("Красный")
    traffic.running()
    """2. Реализовать класс Road (дорога). определить атрибуты: length (длина), width (ширина); значения атрибутов должны 
    передаваться при создании экземпляра класса; атрибуты сделать защищёнными; определить метод расчёта массы асфальта, 
    необходимого для покрытия всей дороги; использовать формулу: длина*ширина*масса асфальта для покрытия одного кв. 
    метра дороги асфальтом, толщиной в 1 см*число см толщины полотна; проверить работу метода. 
    Например: 20 м*5000 м*25 
    кг*5 см = 12500 т. """

    road = Road(20, 5000)
    print(f"Вес асфальта = {road.weight(5)} кг")

    """3. Реализовать базовый класс Worker (работник). определить атрибуты: name, surname, position (должность), 
    income (доход); последний атрибут должен быть защищённым и ссылаться на словарь, содержащий элементы: оклад и премия, 
    например, {"wage": wage, "bonus": bonus}; создать класс Position (должность) на базе класса Worker; в классе Position 
    реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учётом премии (get_total_income); 
    проверить работу примера на реальных данных: создать экземпляры класса Position, передать данные, проверить значения 
    атрибутов, вызвать методы экземпляров. """

    position = Position("Роман", "Марченко", "Сантехник", {"wage": 100000, "bonus": 25000})
    print(f"Сотрудник: {position.get_full_name()}")
    print(f"Доход = {position.get_total_income()}")

    # Тест 1 с ошибкой
    position = Position("Роман", "Марченко", "", {"wage": 100000, "bonus": 25000})
    print("Тест 1 ---")
    print(f"Сотрудник: {position.get_full_name()}")
    print(f"Доход = {position.get_total_income()}")

    # Тест 2 с ошибкой
    print("Тест 2 ---")
    position = Position("Роман", "Марченко", "Сантехник", {"wage": 0, "bonus": 25000})
    print(f"Сотрудник: {position.get_full_name()}")
    print(f"Доход = {position.get_total_income()}")

    # Тест 3 с ошибкой
    print("Тест 3 ---")
    position = Position("Роман", "Марченко", "Сантехник", {"wage": 100000})
    print(f"Сотрудник: {position.get_full_name()}")
    print(f"Доход = {position.get_total_income()}")

    """4. Реализуйте базовый класс Car. у класса должны быть следующие атрибуты: speed, color, name, is_police (булево). 
    А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула ( 
    куда); опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar; добавьте в базовый класс метод 
    show_speed, который должен показывать текущую скорость автомобиля; для классов TownCar и WorkCar переопределите метод 
    show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении 
    скорости. Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, 
    выведите результат. Вызовите методы и покажите результат. """

    townCar = TownCar("Юг", 70, "Белый", "Toyota Corona", False)
    townCar.go(70)
    townCar.show_speed()
    townCar.go(60)
    townCar.stop()
    print("-----------")
    sportCar = SportCar("Космическая стартовая площадка", 130, "Красный", "Tesla Roadster")
    sportCar.info()
    sportCar.turn("Марс")
    sportCar.go(52200000)
    print("-----------")
    workCar = WorkCar("Восток", 30, "Зеленый", "Man", False)
    workCar.go(50)
    workCar.show_speed()
    workCar.go(40)
    workCar.stop()
    print("-----------")
    policeCar = PoliceCar("Запад", 70, "Зеленый", "Волга")
    policeCar.go(90)
    policeCar.show_speed()
    policeCar.go(40)
    policeCar.stop()

    """5. Реализовать класс Stationery (канцелярская принадлежность).
    определить в нём атрибут title (название) и метод draw (отрисовка). Метод выводит сообщение «Запуск отрисовки»;
    создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
    в каждом классе реализовать переопределение метода draw. Для каждого класса метод должен выводить уникальное сообщение;
    создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
    """
    # pen = Pen("Красная ручка")
    # pen.draw()
    # pencil = Pencil("Зеленый карандаш")
    # pencil.draw()
    # handle = Handle("Чёрный маркер")
    # handle.draw()