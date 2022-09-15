A, B = map(int,input().split())
C = int(input())

A += (B+C) // 60

if A < 24 and B+C < 60:
    B += C
    print(A, B)

elif A < 24 and B+C >= 60:
    B = (B+C) % 60
    print(A, B)

elif A >= 24 and B+C >= 60:
    A -= 24
    B = (B+C) % 60
    print(A, B)