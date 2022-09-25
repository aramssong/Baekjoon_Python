N = int(input())
lst = list(map(int, input().split()))
new_lst = []
avg = 0

for i in lst:
    new_lst.append(i/max(lst)*100)

for j in new_lst:
    avg += j
print(avg/N)