# X는 분수의 위치를 나타냄
X = int(input())

group = 0   # 최대 숫자를 기준으로 만든 그룹의 갯수
cnt = 0     # 전체 수의 갯수

# 분수가 위치한 그룹과 그 그룹의 갯수를 구하기
while X > cnt:
    group += 1
    cnt += group
    
# 그룹 마지막 수에서 X번째 분수까지의 순서 차
# ex. gap = 1 : 마지막 수에서 1만큼 앞에 있는 수
gap = cnt - X

# 그룹이 짝수일 때 (분자가 1씩 커짐)
if group % 2 == 0:
    top = group - gap  
    under = gap + 1

# 그룹이 홀수일 때 (분자가 1씩 작아짐)
else:
    top = gap + 1
    under = group - gap
    
print(f'{top}/{under}')