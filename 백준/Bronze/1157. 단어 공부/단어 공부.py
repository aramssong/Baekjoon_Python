N = input().upper()

dist = list(set(N))
lst = list(N)
num = [0] * len(lst)

for i in lst:
    if i in dist:
        num[dist.index(i)] += 1

if num.count(max(num)) == 1:
    print(dist[num.index(max(num))])
else:
    print('?')