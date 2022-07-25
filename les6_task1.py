# Написать программу, которая считывает из консоли путь до файла и файл и
# выводит самое длинное слово, если такое в файле есть, и выводит "Not Found" если такого слова нет

from f_les6_task1 import long_word, read_data

while True:
    path = input("Введите путь к файлу:")
    # Если введен "0" - завершаем программу
    if path != "0":
        # запуск функции чтения файла
        data = read_data(path)
        # код возврата - "-1", если файл открыть не удалось (например: открываем не существующий файл)
        if data != -1:
            # запуск функции определения самого длинного слова
            res = long_word(data)
            if res != "Not found":
                print(f"В самом длинном слове '{res[0]}' {res[1]} букв")
            else:
                print("Слов не найдено.")
    else:
        break


