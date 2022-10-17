T = int(input())

for _ in range(T):
    H, W, N = map(int, input().split())

# 방번호 YYXX (Y : 층 수, X : 번호)
    Y = N % H
    X = (N // H) + 1

    if Y == 0:
        Y = H
        X = (N // H)

    answer = Y * 100 + X
    print(answer)