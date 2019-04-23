def prastevilo(n):
    delitelji = [1]
    for i in range(2, n+1):
        if n % i == 0:
            delitelji.append(i)
    return len(delitelji) == 2


for i in range(2,201):
    if prastevilo(i):
        print(i)