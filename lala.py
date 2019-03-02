a = [int(el) for el in input().split()]
a[a.index(max(a))], a[a.index(min(a))] = a[a.index(min(a))], a[a.index(max(a))]
for el in a:
    print(el)
