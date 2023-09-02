import sys
from pprint import pprint
sys.stdin = open('input.txt')
T = int(input())

for tc in range(1, T+1):
    P, A, B = list(map(int, input().split()))
    l = 1
    r = P
    count_a = 0
    while True:
        c = int((l+r)/2)
        if A < c:
            r = c
            
        elif A > c:
            l = c
            
        else:
            break

        count_a += 1

    l = 1
    r = P
    count_b = 0
    while True:
        c = int((l+r)/2)
        if B < c:
            r = c
            
        elif B > c:
            l = c
            
        else:
            break

        count_b += 1

    print(count_a, count_b)