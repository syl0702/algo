import sys
from pprint import pprint
sys.stdin = open('input.txt')
T = int(input())

for tc in range(1, T+1):
    E, N = list(map(int, input().split()))
    nodes = list(map(int, input().split()))
    tree = [[0]*(E+1) for _ in range(E+1)]
    # pprint(tree)
    temp = []
    # for i in range(1, E+1):
    #     print()

    for k in range(0, len(nodes), 2):
        temp.append([nodes[k], nodes[k+1]])
    print(temp)
    # print(len(temp))

    # print(tree[0][3])
    # for i in range(E):
    #     start = temp[i][0]
    #     end = temp[i][1]
    #     print(start, end)
    #         tree[start][end] = 1
    #         # tree[i+1].append(temp[i][1])
    #         # tree.insert(temp[i][0], temp[i][1])
    #     else:
    #         pass
    # print(tree)