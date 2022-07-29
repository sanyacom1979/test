

def del_comment(src,dst):
    try:
        fs = open(src, encoding="utf-8")
        fd = open(dst, encoding="utf-8", mode="w")
    except FileNotFoundError:
        print("Файл не найден")
    else:
        for line in fs:
            if line[0] != "#":
             fd.write(line)
        fs.close()
        fd.close()
        print("OK")

src = input("Путь к источнику:")
dst = input("Путь к назначению:")
del_comment(src, dst)