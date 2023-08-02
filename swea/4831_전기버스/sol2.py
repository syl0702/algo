import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    K, N, M = map(int, input().split())
    counting_nums = 0
    charge_stations = list(map(int, input().split()))
    print(charge_stations)

    for j in charge_stations:
        j = 0
        if j < N:
            j += 1
            print(j)

        if j == K:
            counting_nums += 1
            charge_stations[j] = charge_stations[j+1]
            if j % K == 1 or j % K == 2:
                counting_nums += 1
                charge_stations[j] = charge_stations[j+1]
                    
            else:
                counting_nums = 0
            
        # result = counting_nums
        # print(f'#{tc} {result}')