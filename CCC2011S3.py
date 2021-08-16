T = int(input())


def crystals(m, x):
    if m >= 1:
        p = pow(5, m-1)
        lpos = x//p
        if lpos == 0 or lpos == 4:
            return 0
        elif lpos == 1 or lpos == 3:
            return p  + crystals(m-1, x%p)
        elif lpos == 2:
            return p*2 + crystals(m-1, x%p)
        else:
            return p
    return 0


for i in range(T):
    ss = input().split()
    m = int(ss[0])
    x = int(ss[1])
    y = int(ss[2])

    if y < crystals(m, x):
        print("crystal")
    else:
        print("empty")