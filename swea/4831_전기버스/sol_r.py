import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    K, N, M = map(int, input().split())

    count = 0
    bus_stop = list(map(int, input().split()))
    start = 0
    for i in range(N):
        if start + K in bus_stop:
            start += K
            count += 1

        elif start+K not in bus_stop:
            if start+K-1 in bus_stop:
                start += K-1
                count+= 1
    

        elif start > bus_stop[-1]:
            break

    print(count)