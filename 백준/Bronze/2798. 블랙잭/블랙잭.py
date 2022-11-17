N, M = map(int, input().split())
card = list(map(int, input().split()))

answer = []
for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            hap = card[i] + card[j] + card[k]

            if hap <= M:
                answer.append(hap)
            else:
                continue
print(max(answer))