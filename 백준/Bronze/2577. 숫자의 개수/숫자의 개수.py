A = int(input())
B = int(input())
C = int(input())

lst = [0]*10

for i in str(A*B*C):
    lst[int(i)] += 1

print(*lst, sep = '\n')