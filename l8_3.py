def delitel(n):
    l_del = []
    for i in range(1, n):
        if n % i == 0:
            l_del.append(i)
    return l_del

def perf_num(n):
    l_del = delitel(n)
    s = 0
    for i in l_del:
        s += i
    if s == n:
        return True
    else:
        return False

l = []

for i in range(1, 10000):
    if perf_num(i) == True:
        l.append(i)
print(f"Cписок совершенных чисел {l}")

