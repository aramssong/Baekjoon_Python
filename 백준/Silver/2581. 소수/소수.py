M = int(input())
N = int(input())

lst = []

for i in range(M, N+1):
    count = 0
    for j in range(1, i+1):
        if i % j == 0:
            count += 1
    if count == 2:
        lst.append(i)

if lst:
    print(sum(lst))
    print(min(lst))
if not lst:
    print(-1)