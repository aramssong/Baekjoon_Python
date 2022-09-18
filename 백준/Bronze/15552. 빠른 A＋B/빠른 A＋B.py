import sys

T = int(input())

lst = []

for _ in range(T):
    a, b = map(int, sys.stdin.readline().split())
    lst.append(a+b)

for j in range(len(lst)):
    print(lst[j])