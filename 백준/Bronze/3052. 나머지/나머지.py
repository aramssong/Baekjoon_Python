lst = []

for _ in range(10):
    N = int(input())
    lst.append(N%42)
print(len(list(set(lst))))