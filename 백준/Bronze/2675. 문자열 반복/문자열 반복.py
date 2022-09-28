T = int(input())
for _ in range(T):
    R, S = input().split()

    P = []
    for i in S:
        P.append(i*int(R))
    print(*P, sep = '')