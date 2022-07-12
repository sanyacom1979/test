l = [int(i) for i in input().split()]
l1 = []
for i in l:
    if l1.count(i) == 0:
        l1.append(i)
print(l1)
