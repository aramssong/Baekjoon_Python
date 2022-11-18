while True:
    lst = list(map(int, input().split()))

    if sum(lst) == 0:
        break
    
    max_num = max(lst)
    lst.remove(max_num)
    if lst[0]**2 + lst[1]**2 == max_num**2:
        print('right')
    else:
        print('wrong')