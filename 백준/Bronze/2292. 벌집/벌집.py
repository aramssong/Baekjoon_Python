# 1 (1개)
# 2 ~ 7 (6개)
# 8 ~ 19 (12개)
# 20 ~ 37 (18개)


N = int(input())

num = 1     # 벌집 칸의 수
layer = 1   # 벌집 층의 수

# N이 벌집 칸의 수 이상이 될 경우 반복 종료
while N > num:
    num += 6 * layer  # 벌집 한 층씩 지날수록 6칸씩 증가
    layer += 1        # 벌집 층도 1층씩 증가

print(layer)