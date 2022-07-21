# Задачка 2.
#
# программа интерактивной работы с консолью
#
# add <Имя> <Фамилия> Добавить ученика
# all Вывести список учеников Список
# mark <Оценка> <Номер> Добавить ученику оценку

#Дополнительные команды

#edit <Номер> <Имя> <Фамилия> Изменяет имя
#delete <Номер> Удаляет ученика
#average Список со средним баллом список


from f_les5_task2 import l_add, l_out, l_mark, l_edit, l_del, l_average

# пока пустой словарь
dict = {}
# начальный номер ученика
numb = 1
# ввод команд в цикле
while True:
    cmd = input("Введите команду:").split()
    # при команде "exit" прерываем работу
    if cmd[0] == "exit":
        break
    # добавляем ученика
    elif cmd[0] == "add":
        dict = l_add(cmd[1] + " " + cmd[2], numb,  dict)
        numb += 1
    # выводим список учеников с оценками
    elif cmd[0] == "all":
        l_out(dict)
    # добавляем ученику оценку
    elif cmd[0] == "mark":
        dict = l_mark(int(cmd[1]), int(cmd[2]), dict)
    # меняем имя и(или) фамилию у ученика
    elif cmd[0] == "edit":
        dict = l_edit(int(cmd[1]), cmd[2] + " " + cmd[3], dict)
    # удаляем ученика
    elif cmd[0] == "delete":
        dict = l_del(int(cmd[1]), dict)
    # средний балл
    elif cmd[0] == "average":
        l_average(dict)
    # введена команда не из перечня
    else:
        print("Не понял! Повторите команду!")