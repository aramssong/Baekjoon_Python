hap = []

while True:
    A, B = map(int, input().split())

    if A == 0 and B == 0:
        break
    else:
        hap.append(A+B)

print(*hap, sep = '\n')