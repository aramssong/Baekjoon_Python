N = int(input())

bag = 0

# N이 5의 배수일 때
while N >= 0:
    if N % 5 == 0:
        bag += N // 5
        break

    N -= 3
    bag += 1

else:
    bag = -1

print(bag) 