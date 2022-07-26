a = ["a001", "a002", "a003"]
b = ["Иван Иванов", "Петр Петров", "Сидор Сидоров"]
c = [55, 70, 88]
dict = {}
dict1 = {}
l = []
for k, v in zip(b, c):
    dict[k] = v
for k, k1, v1 in zip(a, dict.keys(), dict.values()):
    dict1[k] = {k1 : v1}
l.append(dict1)
print(l)