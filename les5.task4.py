s = input()
dict = {}
for i in s:
    dict.update({i : s.count(i)})
print(dict)
