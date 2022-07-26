
l = [int(i) for i in input().split()]

min = 999999
max = 0

for i in range(len(l)):
    if l[i] > max:
        max = l[i]
        el_max = i
    if l[i] < min:
        min = l[i]
        el_min = i

print(f"До {l}")

k = l[el_min]
l[el_min] = l[el_max]
l[el_max] = k

print(f"После {l}")



