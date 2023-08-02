import sys
sys.stdin = open('input.txt')

T = int(input())


for tc in range(1, T+1):
    result = []
    N, M = map(int, input().split())
    numbers = list(map(int, input().split()))

    for i in range(N-M+1):

        result.append(sum((numbers[i:i+M])))

    
    answer = max(result)-min(result)
    print(f'#{tc} {answer}')