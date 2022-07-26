a = ["Алексендр", "Михаил", "Антон"]
b = ["Пушкин", "Лермонтов", "Чехов"]
dict = {}
for k, v in zip(a, b):
    dict[k] = v
print(dict)