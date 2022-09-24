lst = []

for _ in range(9):
    N = int(input())
    lst.append(N)

print(max(lst), lst.index(max(lst))+1, sep = '\n')