import sys

N = int(sys.stdin.readline())

stack = []

for _ in range(N):
    order = sys.stdin.readline().split()

    if order[0] == 'push':
        stack.append(order[1])
    
    elif order[0] == 'pop':
        if len(stack) != 0:
            print(stack.pop()) # pop에서 인덱스를 생략한 경우에는 마지막 값을 취득하고 삭제
        else:
            print(-1)
    
    elif order[0] == 'size':
        print(len(stack))
    
    elif order[0] == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    
    elif order[0] == 'top':
        if len(stack) != 0:
            print(stack[-1])
        else:
            print(-1)