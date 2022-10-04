from string import ascii_uppercase

W = input()
num = 0

alpha_list = list(ascii_uppercase)
num_list = [2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 9, 9, 9, 9]

for i in W:
    num += num_list[alpha_list.index(i)] + 1

print(num)