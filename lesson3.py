def run():
    print("Практическое задание 3 ----------")

    """1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление. Числа 
    запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль. """

    while True:
        isCont = input("Продолжить (y/n)? ")
        if isCont == 'y':
            while True:
                a = input("Ввведите делимое = ")
                if not a.isdigit():
                    print("Введенное значение не является числом. Введите еще раз")
                else:
                    a = float(a)
                    break

            b = 0
            while b == 0:
                while True:
                    b = input("Ввведите делитель = ")
                    if not b.isdigit():
                        print("Введенное значение не является числом. Введите еще раз")
                    else:
                        b = float(b)
                        break
            print(f"Результат = {div(a, b)}")

        elif isCont == 'n':
            break

    """2. Выполнить функцию, которая принимает несколько параметров, описывающих данные пользователя: имя, фамилия, 
    год рождения, город проживания, email, телефон. Функция должна принимать параметры как именованные аргументы. 
    Осуществить вывод данных о пользователе одной строкой. """

    print(DataUserFormat(firstName="Гайбадулы", lastName="Исламобадов",
                   birthDate=1983, townLive="Алматы", eMail="g.sarsenbin@gmail.com", phone="+7-777-123-4567")

    """3. Реализовать функцию my_func(), которая принимает три позиционных аргумента и возвращает сумму наибольших 
    двух аргументов. """

    print(my_func(10, 20, 30))

    """4. Программа принимает действительное положительное число x и целое отрицательное число y. Выполните 
    возведение числа x в степень y. Задание реализуйте в виде функции my_func(x, y). При решении задания нужно 
    обойтись без встроенной функции возведения числа в степень. Подсказка: попробуйте решить задачу двумя способами. 
    Первый — возведение в степень с помощью оператора **. Второй — более сложная реализация без оператора **, 
    предусматривающая использование цикла. """
    x = 0
    y = 0
    while True:
        try:
            x = float(input("Введите действительное положительное число "))
        except TypeError:
            print("Ошибка типа")
        if x <= 0:
            print("Число должно быть положительным!")
        else:
            break
    while True:
        try:
            y = int(input("Введите целое отрицательное число "))
        except TypeError:
            print("Ошибка типа")
        if y > 0:
            print("Число должно быть положительным!")
        else:
            break
    print(f"Результат 1 = {iVeGotThePower(x, y)}")
    print(f"Результат 2 = {iVeGotTheMegaPower(x, y)}")

    """5. Программа запрашивает у пользователя строку чисел, разделённых пробелом. При нажатии Enter должна 
    выводиться сумма чисел. Пользователь может продолжить ввод чисел, разделённых пробелом и снова нажать Enter. 
    Сумма вновь введённых чисел будет добавляться к уже подсчитанной сумме. Но если вместо числа вводится специальный 
    символ, выполнение программы завершается. Если специальный символ введён после нескольких чисел, то вначале нужно 
    добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу. """

    cont = True
    resSum = 0
    while cont:
        numbersStr = input("Введите строку чисел, разделенных пробелом. (Символ 'Q' - стоп) ")
        sumNum, cont = sumNumbers(numbersStr)
        resSum += sumNum
        print(f"Промежуточная сумма = {resSum}")
    print(f"Результат = {resSum}")

    """6. Реализовать функцию int_func(), принимающую слова из маленьких латинских букв и возвращающую их же, 
    но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text. """

    print(int_func("string"))

    """7. Продолжить работу над заданием. В программу должна попадать строка из слов, разделённых пробелом. Каждое 
    слово состоит из латинских букв в нижнем регистре. Нужно сделать вывод исходной строки, но каждое слово должно 
    начинаться с заглавной буквы. Используйте написанную ранее функцию int_func(). """

    data = input("Введите строку ")
    dataRes = []
    words = data.split()
    for w in words:
        dataRes.append(int_func(w))
    print(" ".join(dataRes))

# --- функции ---
def div(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Делитель должен быть больше 0"
    except TypeError:
        return "Невалидный тип данных"


def DataUserFormat(**kwarqs):
    return f"Имя: {kwarqs['firstName']} Фамилия: {kwarqs['lastName']} Год рождения: {kwarqs['birthDate']} " \
           f"Город проживания: {kwarqs['townLive']} EMail: {kwarqs['eMail']} Телефон: {kwarqs['phone']}"


def my_func(a1, a2, a3):
    data = [a1, a2, a3]
    data.sort(reverse=True)
    return sum(data[:2])


def iVeGotThePower(x, y):
    return x ** y


def iVeGotTheMegaPower(x, y):
    res = 1
    while y < 0:
        res *= 1 / x
        y += 1
    return res


def sumNumbers(numbers_str):
    data = numbers_str.split()
    res = 0
    for elem in data:
        if elem:
            try:
                if elem == 'Q':
                    return res, False
                else:
                    res += int(elem)
            except ValueError:
                continue
    return res, True


def int_func(s):
    return s.capitalize()
