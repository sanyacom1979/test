# функция добавления ученика в список
def l_add(st, numb, dict):
    dict[numb] = {st : []}
    print("OK")
    return dict


# функция вывода списка учеников
def l_out(dict):
    for k1, v1 in dict.items():
        for k2, v2 in v1.items():
            if v2 == []:
                print(f"{k1}. {k2}")
            else:
                print(f"{k1}. {k2}", end = " ")
                for i in range(len(v2)):
                    if i == len(v2) - 1:
                        print(f"{v2[i]}")
                    else:
                        print(f"{v2[i]},", end = " ")



# функция добавления оценки
def l_mark(mark, numb, dict):
    for v in dict[numb].values():
        v.append(mark)
    print("OK")
    return dict


# функция изменения имени
def l_edit(numb, new_name, dict):
    for v in dict[numb].values():
        dict[numb] = {new_name : v}
    print("OK")
    return dict

# функция удаления ученика
def l_del(numb, dict):
    del dict[numb]
    print("OK")
    return dict

# функция вычисления среднего балла
def l_average(dict):
    for k1, v1 in dict.items():
        for k2, v2 in v1.items():
            if v2 == []:
                print(f"{k1}. {k2}")
            else:
                print(f"{k1}. {k2}", end = " ")
                s = 0
                for i in v2:
                    s += i
                print(f"{s / len(v2)}")

