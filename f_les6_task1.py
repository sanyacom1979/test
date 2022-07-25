from os.path import exists


# функция считывания файла
def read_data(path):
    if exists(path):
        data = []
        with open(path, encoding="utf-8") as f:
            for line in f:
                data.append(line.strip())
        return data
    else:
        print("Потытка открыть не существующий файл!")
        return -1


# функция определения самого длинного слова
def long_word(data):
    max_len = 0
    if data != []:
        for i in data:
            if len(i) > max_len:
                max_len = len(i)
                max_word = i
        return max_word, max_len
    else:
        return "Not found"

