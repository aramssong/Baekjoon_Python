T = int(input())

for _ in range(T):
    floor = int(input())
    num = int(input())

    # 0층 리스트 만들기
    zero = []
    for i in range(1, num+1):
        zero.append(i)

    # 0층부터 한 층씩 사람수 업데이트
    for j in range(floor):
        for n in range(1, num):
            zero[n] += zero[n-1]
    print(zero[-1])