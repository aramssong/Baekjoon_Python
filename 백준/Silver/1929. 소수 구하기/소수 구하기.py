# '에라토스테네스의 체' 알고리즘 활용

M, N = map(int, input().split())

for i in range(M, N+1):
    # 1은 소수가 아니므로 제외
    if i == 1:
        continue
    # 2부터 i의 제곱근까지만 소수인지 검증 → 빠르게 검증 가능
    for j in range(2, int(i**0.5)+1):
        if i % j == 0:
            break
    else:
        print(i)