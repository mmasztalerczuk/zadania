n = range(1000000000)


def complexity_1(n):
    return n[0]

def complexity_2(n, a):
    l = 0
    p = len(n)
    q = 1
    while l != p:
        print(q, l, p)
        q += 1
        mid = (l+p)//2
        if n[mid] > a:
            p = mid
        elif n[mid] < a:
            l = mid
        else:
            print(n[mid], mid)
            return

def complexity_3(n):
    for i in range(n):
        for j in range(n):
            print(i+j)