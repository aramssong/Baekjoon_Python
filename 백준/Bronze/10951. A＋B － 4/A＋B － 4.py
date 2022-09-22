hap = []

while True:
    try:
        A, B = map(int, input().split())
        hap.append(A+B)
    except:
        break

print(*hap, sep = '\n')