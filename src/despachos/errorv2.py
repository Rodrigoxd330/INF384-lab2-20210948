def malogrando:
    a = 3
    b = 2
    c  = 0
    for i in range(1,30):
        a = a*i + b
        b = b*i + a
        if (a > b):
            c = c + 1
        else:
            c = c - 1
    if (c > 0):
        print("Gano a")
    if (c == 0):
        print("Empate")
    if (c < 0):
        print("Gano b")
    return c