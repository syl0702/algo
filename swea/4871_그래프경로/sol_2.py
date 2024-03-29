import sys
from pprint import pprint
sys.stdin = open('input.txt')
T = int(input())

for tc in range(1, T+1):
    # V: 노드 수/ E: 간선 수
    V, E = list(map(int, input().split()))

    # V + 1 만드는 이유: 인덱스와 숫자를 정확히 매치하기 위함.
    nodes = [[0]*(V+1) for _ in range(V+1)]
    # pprint(nodes)

    # 인접 행렬 방식으로 그래프 저장
    # 간선의 갯수만큼 반복 진행.
    for line in range(E):
        start, end = list(map(int, input().split()))
        nodes[start][end] = 1
    # pprint(nodes)
        
    # S: 출발노드/ G: 도착노드
    S, G = list(map(int, input().split()))

    # 방문 체크용 리스트
    check_list = [False] * (V+1)

    # dfs 구현 위한 stack
    stack = []

    now = S
    now = check_list[now] = True
    stack.append(now)

    result = 0

    while len(stack):
        now = stack.pop()
        check_list[now] = True

        # 가로의 길이만큼 반복문을 돌려. link는 해당하는 idx 번호
        for link in range(V+1):
            # now를 기준으로 연결되어 있다면
            if nodes[now][link] == 1:
                # 방문하지 않았다면
                if not check_list[link]:
                    # 목적지가 연결되어 있다면
                    if link == G:
                        result = 1
                    
                    # stack에 추가
                    stack.append(link)