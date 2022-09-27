N = int(input())
num = input()

lst_num = 0

for i in range(len(num)):
    lst_num += int(str(num)[i])

print(lst_num)