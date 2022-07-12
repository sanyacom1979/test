
l = [int(i) for i in input().split()]
max = []
for i in range(1, len(l) - 1):
    if l[i] > l[i - 1] and l[i] > l[i + 1]:
        max.append(l[i])

print(max)


