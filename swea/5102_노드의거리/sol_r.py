import sys
from pprint import pprint
sys.stdin = open('input.txt')
T = int(input())

for tc in range(1, T+1):
    V, E = list(map(int, input().split()))

    nodes = [[0]*(V+1) for _ in range(V+1)]

    for line in range(E):
        start, end = list(map(int, input().split()))
        nodes[start][end] = 1
        nodes[end][start] = 1
    # pprint(nodes)

    S, G = list(map(int, input().split()))

    passed = [0] * (V+1)
    temp = []
    now = S
    passed[now] = 1
    temp.append(now)
    distance = 0

    while len(temp):
        now = temp.pop(0)
        passed[now] = 1
        for link in range(V+1):
            if nodes[now][link] == 1:
                if not passed[link]:
                    if link == G:
                        print(distance)
                    temp.append(link)
                    distance += 1
                


    # print(distance)