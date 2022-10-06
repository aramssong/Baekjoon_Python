A, B, C = map(int, input().split())

if C - B > 0:
    cnt = A // (C-B) + 1
else:
    cnt = -1
print(cnt)