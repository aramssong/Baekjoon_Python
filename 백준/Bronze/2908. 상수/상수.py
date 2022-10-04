A, B = map(int, input().split())

new_num = []
new_num.append(str(A)[-1]+str(A)[-2]+str(A)[-3])
new_num.append(str(B)[-1]+str(B)[-2]+str(B)[-3])

print(max(new_num))