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
                        print(f"{v2[i]}", end = " ")
                    else:
                        print(f"{v2[i]},", end = " ")
                print("")


# функция добавления оценки
def l_mark(mark, numb, dict):
    for v in dict[numb].values():
        v.append(mark)
    print("OK")
    return dict