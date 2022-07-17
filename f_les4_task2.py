from matplotlib import pyplot as plt


def s_plit(str):
    return str.split()


def graf(a, b, c, n):
    # проверяем а на не ноль
    if a == 0:
        raise Exception("А не должно быть нулевым")
    # генерируем 2 списка
    x = [i for i in range(-n, n + 1)]                              # ось абцисс
    y = [(a * i ** 2) + (b * i) + c for i in range(-n, n + 1)]     # ось ординат
    # строим график
    plt.plot(x, y)
    plt.show()
