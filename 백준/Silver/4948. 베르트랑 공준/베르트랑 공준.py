## 소수인지 판단하는 함수
def check_sosu(x):
    # 1은 모든 수의 약수이므로 False
    if x == 1:
        return False
    # 2~제곱근 수까지 약수가 있으면 False
    for i in range(2, int(x**0.5)+1):
        if x % i == 0:
            return False
    # 이외에는 소수
    return True

## 소수 구하기 (위의 함수를 활용)
lst = list(range(2, 2*123456))  # 문제에서 제한한 범위
sosu = []  # 판단한 소수를 담는 리스트

# 2부터 2n까지의 수가 담긴 lst에서 수를 하나씩 꺼내 소수인지 확인
# 소수가 맞으면 sosu 리스트에 추가
for num in lst:
    if check_sosu(num):
        sosu.append(num)

## 입력 및 출력
while True:
    n = int(input())
    if n == 0:
        break
    
    # sosu 리스트에서 수를 하나씩 꺼내 n보다 크고 2n보다 작거나 같으면 count에 1 더함
    count = 0
    for s in sosu:
        if n < s <= n*2:
            count += 1
    print(count)