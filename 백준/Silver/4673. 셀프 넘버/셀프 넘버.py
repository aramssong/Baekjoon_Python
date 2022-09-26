number = set(range(1, 10001))
generated_num = set()

for num in number:
    for n in str(num):
        num += int(n)
    generated_num.add(num)

answer = sorted(number - generated_num)
for a in answer:
    print(a)