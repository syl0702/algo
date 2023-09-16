import sys
from pprint import pprint
sys.stdin = open('input.txt')
T = int(input())

for tc in range(1, T+1):
    N, M = list(map(int, input().split()))
    Ci = list(map(int, input().split()))
    
    before = []
    after = []
    for i in range(M):
        
        before.append([Ci[i], i+1])
    # print(before)
    oven = before[:N]
    pan = before[N:]

    while len(oven) > 1:
        pizza = oven.pop(0)
        pizza[0] //= 2
        if pizza[0] == 0:
            if pan:
                oven.append(pan.pop(0))
        # else:
        #     oven.append(pizza)

    print(oven[0][1])
    
