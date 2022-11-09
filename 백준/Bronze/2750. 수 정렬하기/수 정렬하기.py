N = int(input())

lst = []
for _ in range(N):
    M = int(input())
    lst.append(M)
lst.sort()
print(*lst, sep = '\n')