num = int(input())

for _ in range(num):
    N = list(input())

    count = 0
    add_value = 1

    for i in N:
        if i == "O":
            count += add_value
            add_value += 1
        else:
            add_value = 1
    print(count)