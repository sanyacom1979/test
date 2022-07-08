# Функция считывания даты
def r_date():
    d, m, y = input().split(".")
    return int(d), int(m), int(y)

# Функция проверки даты

def ch_date(d, m ,y):
    msg = []  # для вывода сообщения об ошибке
    r_y = 0   # результат по году
    r_m = 0   # результат по месацу
    r_d = 0   # результат по дню
# проверка года (условимся, что правильный диапазон 1900 - 2099)
    if y < 1900 or y > 2099:
        r_y = 1
        msg.append("Incorrect Year")
# проверка месяца (должен быть от 1 до 12)
    if m < 1 or m > 12:
        r_m = 1
        msg.append("Incorrect Month")
# проверка дня (взависимости от месяца:
# январь - 31 день, февраль - 28 или 29 взависимости от года и т.д
    if (m == 1 or m == 3 or m == 5 or m == 7 or
    m == 8 or m == 10 or m == 12) and (d < 1 or d > 31):
        r_d = 1
        msg.append("Incorrect Day")
    elif (m == 4 or m == 6 or m == 9 or m == 11) and (d < 1 or d > 30):
        r_d = 1
        msg.append("Incorrect Day")
    elif m == 2 and y % 4 == 0 and (d < 1 or d > 29):
        r_d = 1
        msg.append("Incorrect Day")
    elif m == 2 and y % 4 != 0 and (d < 1 or d > 28):
        r_d = 1
        msg.append("Incorrect Day")
    elif d < 1 or d > 31:
        r_d = 1
        msg.append("Incorrect Day")
    if r_y == 0 and r_m == 0 and r_d == 0:
        return "OK"
    else:
        return "FALSE", msg




