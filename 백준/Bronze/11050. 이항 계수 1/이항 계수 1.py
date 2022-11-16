def factorial(n):
    num = 1
    for i in range(2, n+1):
        num *= i
    return num

N, K = map(int, input().split())
answer = factorial(N) // (factorial(N-K) * factorial(K))
print(answer)