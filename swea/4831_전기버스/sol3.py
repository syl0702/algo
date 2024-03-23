import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    K, N, M = map(int, input().split())

    bus_stop = list(map(int, input().split()))
    count = 0
    # 현재 버스가 있는 위치: now
    now = 0

    # 충전할 필요가 없이 바로 도착하는 경우
    if K >= N:
        count = 0
    
    # 충전을 하면서 지나가야 하는 경우
    else:
        # 버스가 아직 종점에 도착하지 않았을 경우 계속해서 반복
        while now < N:
            # 현재 위치(now)에서 최대로 갈 수 있는 범위를 찾는다.
            # 최대로 갈 수 있는 범위(now+K)부터 현재 위치까지 반복
            for i in range(now+K, now, -1):
                # 1. 최대 범위가 종점을 넘는 경우
                if i >= N:
                    now = N
                    break

                # 2. 최대 범위가 종점을 넘지 않은 경우