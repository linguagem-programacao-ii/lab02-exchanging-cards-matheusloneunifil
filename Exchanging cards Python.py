while True:
    a, b = input().split()
    if a == b == '0':
        break
    xa = [int(d) for d in input().split()]
    xb = [int(d) for d in input().split()]
    a = set(fa)
    b = set(fb)
    c = b
    f = 0
    if len(a) < len(b):
        c = a
        a = b
    c = [d for d in c if d not in a]
    print(len(c))