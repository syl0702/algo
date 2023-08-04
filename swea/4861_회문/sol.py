import sys
sys.stdin = open('input.txt')
from pprint import pprint

T = int(input())

for tc in range(1, T+1):
    N,M = list(map(int, input().split()))

    string_map = []
    for string in range(N):
        # 'GOFFAKWFSM'식
        string_map.append(input())
    pprint(string_map)
        # 따로 보려면 like 'G' 'F'
        # string_map.append(list(input()))
    
    result = []
    #반복작업
    # 가로 검증 세로는 모두 확인하고 가로는 N-M+1만큼 반복
    # 가로 기준점/ 회문의 시작점을 잡기 위한 코드
    for row in range(N):
        for col in range(N-M+1):
            # print(string_map[row][col]) 나의 위치

            for i in range(M//2):
                # front : 앞글자 부터 한칸씩 (i의 증가량)증가
                f = string_map[row][col + i]
                # back : 뒷글자 부터 한칸씩 (i의 감소량) 감소
                b = string_map[row][col + M -1 -i]

                # 앞뒤가 똑같다면
                if f == b:
                    continue
                # 똑같지 않다면
                else:
                    break
            # for 문을 끝까지 도는 경우/ break를 만나지 않은 경우 => 회문 찾았다!
            else:
                
                for a in range(M):
                    result.append(string_map[row][col+a])

        # 세로 기준점 / 회문의 시작점을 잡기 위한 코드
    for col in range(N):
        for row in range(N-M+1):

            for i in range(M//2):
                # front : 앞글자 부터 한칸씩 (i의 증가량)증가
                f = string_map[row + i][col]
                # back : 뒷글자 부터 한칸씩 (i의 감소량) 감소
                b = string_map[row + M -1 - i][col]

                # 앞뒤가 똑같다면
                if f == b:
                    continue
                # 똑같지 않다면
                else:
                    break
            else:
                for a in range(M):
                    result.append(string_map[row+a][col])

    answer = ''.join(result)
    print(f'#{tc} {answer}')              