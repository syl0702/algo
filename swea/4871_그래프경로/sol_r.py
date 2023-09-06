import sys
from pprint import pprint
sys.stdin = open('input.txt')
T = int(input())

for tc in range(1, T+1):
    V, E = list(map(int, input().split()))

    nodes = [[0] * (V+1) for i in range(V+1)]

    for line in range(E):
        start, end = list(map(int, input().split()))
        nodes[start][end] = 1
        # pprint(nodes)

    S, G = list(map(int, input().split()))
    check = [False]*(V+1)

    temp = []

    now = S
    check[now] = True
    temp.append(now)
    result = 0

    while len(temp):
        now = temp.pop()
        check[now] = True

        for link in range(V+1):
            if nodes[now][link] == 1:
                if not check[link]:
                    if link == G:
                        result = 1
                    temp.append(link)

    print(f'#{tc} {result}')
                        