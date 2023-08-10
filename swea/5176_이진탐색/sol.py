import sys
from pprint import pprint
sys.stdin = open('input.txt')
T = int(input())

def inorder(idx):
    global count
    if idx <= N:

        # 왼쪽 자식 방문
        inorder(idx * 2)

        # 현재 노드 방문
        tree[idx] = count
        count += 1

        # 오른쪽 자식 방문
        inorder(idx * 2 + 1)
        
for tc in range(1, T+1):
    N = int(input())

    tree = [0] * (N+1)

    count = 1

    # 1번부터 시작해 주세요
    inorder(1)
    print(tree[1])

    

    print(f'#{tc} {tree[1]} {tree[N // 2]}')