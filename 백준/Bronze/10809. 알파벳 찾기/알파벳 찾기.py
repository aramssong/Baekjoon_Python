S = input()

alpha = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k" ,"l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
alpha_num = [0]*26

for i in alpha:
    alpha_num[alpha.index(i)] = S.find(i)

for j in alpha_num:
    print(j, end = ' ')