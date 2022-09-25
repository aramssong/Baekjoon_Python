num = int(input())

for _ in range(num):
    score = list(map(int, input().split()))

    avg = sum(score[1:]) / score[0]
    student = 0

    for i in score[1:]:
        if i > avg:
            student += 1
    
    perc = (student / score[0]) * 100
    print(f'{perc:.3f}%')