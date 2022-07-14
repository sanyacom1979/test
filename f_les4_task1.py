from math import sqrt


def s_plit(str):
    return str.split()


def korny(a, b, c):
    # имеем квадратное уравнение a * x ** 2 + b * x + c = 0, где a != 0
    # проверяем а на не ноль
    if a == 0:
        raise Exception("А не должно быть нулевым")
    # дискриминант
    D = (b ** 2) - (4 * a * c)
    # проверка дискриминанта
    if D > 0:
        # 2 корня
        x1 = (- b + sqrt(D)) / (2 * a)
        x2 = (- b - sqrt(D)) / (2 * a)
        return x1, x2
    elif D == 0:
        # 1 корень
        x = - b / (2 * a)
        return x
    else:
        return "Нет корней"
