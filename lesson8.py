class Date:
    def __init__(self, value):
        if isinstance(value, str):
            self.value = value
        else:
            print("Ошибка! Значение должно быть строкой")

    def extract(self):
        try:
            d, m, y = self.value.split('-')
            return d, m, y
        except Exception as e:
            print(f"Ошибка извлечения: {e}")

    @staticmethod
    def isValid(cls):
        if not isinstance(cls, str):
            print("Ошибка! Значение должно быть строкой")
            return False
        try:
            d, m, y = cls.split('-')
            if not (1 <= int(d) <= 31):
                print("Ошибка! День указан не верно")
                return False
            elif not (1 <= int(m) <= 12):
                print("Ошибка! Месяц указан не верно")
                return False
            elif not (1 <= int(y)):
                print("Ошибка! Год указан не верно")
                return False
        except Exception as e:
            print(f"Ошибка проверки валидации: {e}")
            return False
        return True  # всё ништяг


class DivByZeroException(Exception):
    def __init__(self):
        self.msg = "Ошибка деления на 0"


class CastNumberException(Exception):
    def __init__(self):
        self.msg = "Число должно быть целым"


def castNumber(number):
    if number.isdigit():
        return float(number)
    else:
        raise CastNumberException


class Device:
    def __init__(self, company, model, type_device):
        self.company = company
        self.model = model
        self.type_device = type_device


class Printer(Device):
    def __init__(self, company, model, speed_count):
        super().__init__(company, model, "Принтер")
        self.speed_count = speed_count  # кол-во страниц в минуту

    def info(self):
        print(self.company, self.model, self.type_device, self.speed_count)


class Scanner(Device):
    def __init__(self, company, model, dpi):
        super().__init__(company, model, "Сканер")
        self.dpi = dpi  # разрешение точек на дюйм

    def info(self):
        print(self.company, self.model, self.type_device, self.dpi)


class Copier(Device):
    def __init__(self, company, model, frm):
        super().__init__(company, model, "Копир")
        self.frm = frm  # формат (А4, A3 и т.д.)

    def info(self):
        print(self.company, self.model, self.type_device, self.frm)


def validate(func):  # чесно стырил
    def wrapper(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except ValueError:
            print("Недостаточно техники на складе!")
        except KeyError:
            print("Нет такого типа оргтехники на складе!")
    return wrapper

class Storage:
    devices = {}

    def __init__(self, name):
        self.name = name

    @classmethod
    def check_keys(cls, dev):
        if dev.type_device not in cls.devices:
            cls.devices[dev.type_device] = {}
        if dev.company not in cls.devices[dev.type_device]:
            cls.devices[dev.type_device][dev.company] = {}
        if dev.model not in cls.devices[dev.type_device][dev.company]:
            cls.devices[dev.type_device][dev.company][dev.model] = {}

    @classmethod
    def st_to(cls, dev, device_count):
        cls.check_keys(dev)
        if "cn" not in cls.devices[dev.type_device][dev.company][dev.model]:
            cls.devices[dev.type_device][dev.company][dev.model]["cn"] = device_count
        else:
            cls.devices[dev.type_device][dev.company][dev.model]["cn"] += device_count

    @classmethod
    @validate
    def st_from(cls, dev, device_count):
        if cls.devices[dev.type_device][dev.company][dev.model]["cn"] > device_count:
            cls.devices[dev.type_device][dev.company][dev.model]["cn"] -= device_count
        else:
            raise ValueError  # print("Что-то не хватает на складе такого кол-ва...")

    @classmethod
    def info(cls):
        for key, value in cls.devices.items():
            print(key, value)


class Complex:
    def __init__(self, r, i):
        self.r = r
        self.i = i

    def __add__(self, other):
        return Complex(self.r + other.r, self.i + other.i)

    def __mul__(self, other):
        return Complex(self.r * other.r - self.i * other.i,
                       self.r * other.i + self.i * other.r)

    def __str__(self):
        return f"{self.r} + {self.i}j"


def run():
    """1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата 
    «день-месяц-год». В рамках класса реализовать два метода. Первый, с декоратором @classmethod. Он должен извлекать 
    число, месяц, год и преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить 
    валидацию числа, месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных 
    данных. """

    date = Date("1-2-2022")
    d, m, y = date.extract()
    print(d, m, y)

    if Date.isValid("1-2-2022"):
        print("Значение валидное")
    else:
        print("Значение не валидное")

    if Date.isValid("в-2-2022"):
        print("Значение валидное")
    else:
        print("Значение не валидное")

    if Date.isValid("0-2-2022"):
        print("Значение валидное")
    else:
        print("Значение не валидное")

    if Date.isValid("1-0-2022"):
        print("Значение валидное")
    else:
        print("Значение не валидное")

    if Date.isValid("1-1-0"):
        print("Значение валидное")
    else:
        print("Значение не валидное")

    """2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на ноль. Проверьте его работу на 
    данных, вводимых пользователем. При вводе нуля в качестве делителя программа должна корректно обработать эту 
    ситуацию и не завершиться с ошибкой. """

    a = 10
    b = 0
    try:
        if b == 0:
            raise DivByZeroException
        print(f"Результат = {a / b}")
    except DivByZeroException as e:
        print(f"Ошибка! {e.msg}")

    """3. Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел. 
    Проверить работу исключения на реальном примере. Запрашивать у пользователя данные и заполнять список необходимо 
    только числами. Класс-исключение должен контролировать типы данных элементов списка. """

    superMegaNumberBeautifulAndPerfectList = []
    while True:
        number = input("Введите целое число. Для выхода введите \\q: ")
        if number == "\\q":
            break
        try:
            c = castNumber(number)
            superMegaNumberBeautifulAndPerfectList.append(c)
        except Exception as e:
            print(f"Ошибка! {e.msg}")
    print(f"Ведены данные = {superMegaNumberBeautifulAndPerfectList}")

    """4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс 
    «Оргтехника», который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, 
    сканер, ксерокс). В базовом классе определите параметры, общие для приведённых типов. В классах-наследниках 
    реализуйте параметры, уникальные для каждого типа оргтехники. """

    """5. Продолжить работу над первым заданием. Разработайте методы, которые отвечают за приём оргтехники на склад и 
    передачу в определённое подразделение компании. Для хранения данных о наименовании и количестве единиц 
    оргтехники, а также других данных, можно использовать любую подходящую структуру (например, словарь). """

    """6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных. 
    Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных. 
    Подсказка: постарайтесь реализовать в проекте «Склад оргтехники» максимум возможностей, изученных на уроках по 
    ООП. """

    printer = Printer('HP', "1020", 8)
    printer.info()

    scanner = Scanner("HP", "38-D15", 600)
    scanner.info()

    copier = Copier("Kyocera", "fs1043", "A4")
    copier.info()

    copier2 = Copier("Xerox", "sp5025", "A3")
    copier.info

    Storage.st_to(printer, 10)
    Storage.st_to(scanner, 15)
    Storage.st_to(copier, 7)
    Storage.info()

    Storage.st_from(copier, 3)
    Storage.info()

    Storage.st_from(copier, 4)

    """7. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число». Реализуйте 
    перегрузку методов сложения и умножения комплексных чисел. Проверьте работу проекта. Для этого создаёте 
    экземпляры класса (комплексные числа), выполните сложение и умножение созданных экземпляров. Проверьте 
    корректность полученного результата. """

    c1 = Complex(10, 20)
    c2 = Complex(-20, 10)
    print(f"Сумма чисел: {c1 + c2}")
    print(f"Произведение чисел: {c1 * c2}")
