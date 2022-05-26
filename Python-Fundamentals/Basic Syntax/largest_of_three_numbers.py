n1 = float(input())
n2 = float(input())
n3 = float(input())

if n1 > n2 and n1 > n3:
    print(int(n1))
elif n2 > n1 and n2 > n3:
    print(int(n2))
elif n3 > n1 and n3 > n2:
    print(int(n3))