import sys
from pprint import pprint
sys.stdin = open('input.txt')
T = int(input())

for tc in range(1, T+1):
    # V : 노드 수 / E : 간선 수
    V, E = list(map(int, input().split()))

    nodes = [[0] * (V+1) for _ in range(V+1)]

    # 인접 행렬 방식으로 저장
    for line in range(E):
        start, end = list(map(int, input().split()))
        nodes[start][end] =1
        nodes[end][start] =1
    pprint(nodes)
    

    S, G = list(map(int, input().split()))

    # 방문 체크용 리스트
    check_list = [False] * (V+1)

    # bfs를 구현하기 위한 queue
    queue = []

    # bfs 시작을 하기 위해 시작 노드를 queue에 저장

    now = S
    check_list[now] = True
    queue.append(now)

    # 거리계산을 위한 리스트
    
    distance = [0] * (V+1)
    

    # 큐가 비어 있지 않으면 계속 반복
    while len(queue):

        now = queue.pop(0)
        check_list[now] = True

        # now와 연결된 다른 노드들 순회
        for link in range(V+1):
            if nodes[now][link] == 1:

                # 아직 방문하지 않은 node가 있다면
                if not check_list[link]:
                    # 큐에 추가
                    queue.append(link)

                    # 이전 노드의 거리 + 1
                    distance[link] = distance[now] + 1
    
    print(f'#{tc} {distance[G]}')
    print('====')
