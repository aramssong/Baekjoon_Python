x, y = map(int, input().split())

# 최대공약수 구하기
def gcd(x, y):
    while y != 0:
        x, y = y, x % y
    return x

# 최소공배수 구하기
def lcm(x, y):
    return (x * y) // gcd(x, y)

print(gcd(x, y))
print(lcm(x, y))