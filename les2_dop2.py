# Задача: Вводится n строк, каждая строка – одно слово. Составить из них
# предложение с пробелами и точкой в конце.

# вводим колличество строк
n = int(input())
# пустой список, туда будем заносить строки
l = []
# вводим n строк и записываем в список
print ("Строки:")
for i in range(n):
   l.append(input())
# Объединяем список в одну строку и выводим ее
print(" ".join(l) + ".")


