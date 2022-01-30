import string
import json


def run():
    print("Практическое задание 5 ----------")
    """1. Создать программный файл в текстовом формате, записать в него построчно данные, вводимые пользователем. Об 
    окончании ввода данных будет свидетельствовать пустая строка. """

    fw = open("text.txt", 'w')
    while True:
        s = input("Введите строку: ")
        if len(s) > 0:
            fw.write(s)
        else:
            fw.close()
            break

    """2. Создать текстовый файл (не программно), сохранить в нём несколько строк, выполнить подсчёт строк и слов в 
    каждой строке. """
    fw = open("text2.txt", "w")
    fw.write("А что мне надо? Да просто свет в оконце\n")
    fw.write("А что мне снится? Что кончилась война\n")
    fw.write("Куда иду я? Туда, где светит солнце\n")
    fw.write("Вот только б, братцы, добраться б дотемна\n")
    fw.close()
    fr = open("text2.txt")
    fr_count_line = 0
    fr_count_word = 0
    for line in fr:
        fr_count_line += 1
        fr_count_word += sum([i.strip(string.punctuation).isalpha() for i in line.split()])
    fr.close()
    print(f"В файле {fr_count_line} строк {fr_count_word} слов")

    """3. Создать текстовый файл (не программно). Построчно записать фамилии сотрудников и величину их окладов (не 
    менее 10 строк). Определить, кто из сотрудников имеет оклад менее 20 тысяч, вывести фамилии этих сотрудников. 
    Выполнить подсчёт средней величины дохода сотрудников. Пример файла: 
    
    Иванов 23543.12
    Петров 13749.32"""

    fw = open("text3.txt", "w")
    fw.write("Сарсенбин 70000\n")
    fw.write("Ибрагимов 50000\n")
    fw.write("Чмух 45000\n")
    fw.write("Егоров 47000\n")
    fw.write("Олегов 27000\n")
    fw.write("Иткин 19000\n")
    fw.write("Гроднов 18000\n")
    fw.write("Соловьёв 15000\n")
    fw.write("Икаров 21000\n")
    fw.write("Лобанов 15000\n")
    fw.close()
    fr = open("text3.txt")
    for line in fr:
        data = line.split()
        if float(data[1]) < 20000:
            print(f"{data[0]} {data[1]}")
    fr.close()

    """4. Создать (не программно) текстовый файл со следующим содержимым: One — 1 Two — 2 Three — 3 Four — 4 Напишите 
    программу, открывающую файл на чтение и считывающую построчно данные. При этом английские числительные должны 
    заменяться на русские. Новый блок строк должен записываться в новый текстовый файл. """
    fr = open("text4en.txt")
    fw = open("text4ru.txt", "w")
    for line in fr:
        w = line.split()
        # print(f"{w[0]} {w[1]} {w[2]}")
        # print(translate(w[0]))
        fw.write(f"{translate(w[0])} - {w[2]}\n")
    fr.close()
    fw.close()

    """5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделённых пробелами. 
    Программа должна подсчитывать сумму чисел в файле и выводить её на экран. """
    fw = open("text5.txt", "w")
    for i in range(5):
        fw.write(f"{i} ")
    fw.close()
    fr = open("text5.txt")
    line = fr.readline()
    data = line.split()
    summ = 0
    for i in data:
        summ += int(i)
    fr.close()
    print(f"Сумма = {summ}")

    """6. Сформировать (не программно) текстовый файл. В нём каждая строка должна описывать учебный предмет и наличие 
    лекционных, практических и лабораторных занятий по предмету. Сюда должно входить и количество занятий. 
    Необязательно, чтобы для каждого предмета были все типы занятий. Сформировать словарь, содержащий название 
    предмета и общее количество занятий по нему. Вывести его на экран. Примеры строк файла: Информатика: 100(л) 50(
    пр) 20(лаб). Физика: 30(л) — 10(лаб) Физкультура: — 30(пр) — Пример словаря: {“Информатика”: 170, “Физика”: 40, 
    “Физкультура”: 30} """

    fr = open("text6.txt", "r", encoding='utf-8')
    res = {}
    for line in fr:
        data_name, *data_hours = line.split()
        data_count = [int(data.rstrip('(л)(пр)(лаб)')) for data in data_hours if data != '-']
        res.update({data_name.rstrip(":"): sum(data_count)})
    print(f"Получен словарь = {res}")

    """7. Создать вручную и заполнить несколькими строками текстовый файл, в котором каждая строка будет содержать 
    данные о фирме: название, форма собственности, выручка, издержки. Пример строки файла: firm_1 ООО 10000 5000. 

    Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль. Если фирма получила 
    убытки, в расчёт средней прибыли её не включать. Далее реализовать список. Он должен содержать словарь с фирмами и 
    их прибылями, а также словарь со средней прибылью. Если фирма получила убытки, также добавить её в словарь 
    (со значением убытков). Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}]. 
    
    Итоговый список сохранить в виде json-объекта в соответствующий файл.
    Пример json-объекта:
    [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
    Подсказка: использовать менеджер контекста
    """
    res = []
    fr = open("text7.txt", "r", encoding='utf-8')
    profit_plus = {}
    profit_minus = {}
    profit_avr = []
    for line in fr:
        name, form, earnings, costs = line.rstrip().split()
        # print(name, form, earnings, costs)
        profit = int(earnings) - int(costs)
        if profit > 0:
            profit_avr.append(profit)
            profit_plus.update({name: profit})
        else:
            profit_minus.update({name: profit})
    fr.close()
    res.append(profit_plus)
    res.append(profit_minus)
    res.append({"Average profit": sum(profit_avr)/len(profit_avr)})
    print(res)
    fw = open("text7.json", "w")
    json.dump(res, fw)
    fw.close()

def translate(name):
    return {
        name == 'One': 'Один',
        name == 'Two': 'Два',
        name == 'Three': 'Три',
        name == 'Four': 'Четыре'
    }[True]
