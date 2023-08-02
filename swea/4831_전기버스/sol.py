import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    # K : 최대로 이동 가능한 정류장 수
    # N : 종점
    # M : 충전기가 설치된 정류장 수
    K, N, M = map(int, input().split())

    bus_stop = list(map(int, input().split()))
    count = 0
    # 현재 버스가 있는 위치:now
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

                # 2. 최대범위가 종점을 아직 넘지 않은 경우
                if i in bus_stop:
                    # 가장 뒤에 있는 충전소로 이동
                    now = i

                    # 충전을 하고 이동을 했으니 카운트 증가
                    count += 1

                    # 마지막 충전소를 찾았으니 더 이상 후진할 필요 없음
                    break
            # 현재 위치에서 최대 거리를 찾았는데, 충전소가 없다면? => 도착 불가능
            else:
                count = 0
                now = N

    print(f'#{tc} {count}')

# for tc in range(1, T+1):
#     K, N, M = list(map(int, input().split()))
#     counting_nums = 0
#     charge_stations = list(map(int, input().split()))
    

#     for j in charge_stations:
#         j = 0
#         if j < N:
#             j += 1

#             if j == K:
#                 counting_nums += 1
#                 charge_stations[j] = charge_stations[j+K]

#             elif charge_stations[j] % K != 0:
#                 charge_stations[j] = charge_stations[j-1]
#                 counting_nums += 1
#                 continue

#             else:
#                 charge_stations[j] = charge_stations[j+1]
                    
#                     # if charge_stations[j] == N:
#                     #     break

#     else:
#         break