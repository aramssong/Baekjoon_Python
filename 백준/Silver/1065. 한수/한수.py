def check_hansu(x):
    is_hansu = True
    for i in range(len(x)-2):
        if int(x[i]) - int(x[i+1]) == int(x[i+1]) - int(x[i+2]):
            continue
        else:
            is_hansu = False
    return is_hansu

N = int(input())
num = 0

for x in range(1, N+1):
    if check_hansu(str(x)):
        num += 1
    
print(num)