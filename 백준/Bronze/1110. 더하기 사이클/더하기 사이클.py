N = int(input())

sum = N
num = 0

while True:
    a, b = divmod(sum, 10)
    c = (a+b) % 10
    sum = int(str(b)+str(c))
    num += 1

    if sum == N:
        break

print(num)