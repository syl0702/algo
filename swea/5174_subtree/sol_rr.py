import sys
from pprint import pprint
sys.stdin = open('input.txt')
T = int(input())

for tc in range(1, T+1):
    E, N = list(map(int, input().split()))
    nodes = list(map(int, input().split()))
    left_n = [0]*(E+2)
    right_n = [0]*(E+2)

    for k in range(0, len(nodes), 2):
        parent = nodes[k]
        child = nodes[k+1]
        if left_n[parent] == 0:
            left_n[parent] = child
        else:
            right_n[parent] = child
    # print(left_n, right_n)

    temp = [N]
    count = 0

    while temp:
        now = temp.pop()
        count += 1
        if left_n[now]:
            temp.append(left_n[now])
        
        if right_n[now]:
            temp.append(right_n[now])

    print(count)
