N = input()

alpha = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
count = 0

for i in alpha:
    if i in N:
        N = N.replace(i, "0")
count += len(N)
print(count)