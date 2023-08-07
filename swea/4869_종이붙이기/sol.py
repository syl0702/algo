import sys
sys.stdin = open('input.txt')
T = int(input())

memo = [0, 1, 3]
for tc in range(1, T+1):
    N = int(input()) // 10

    # memo 배열에 출력시킬 값이 없으면 추가
    while N >= len(memo):
        # n-1 배열에 가로로 작은 사각형 두 개 쌓거나 큰 사각형 쌓는 방법 (x2)
        # n-1 배열에 세로로 작은 사각형 쌓는 방법 하나.
        temp = 2 * memo[len(memo)-2] + memo[len(memo)-1]  
        memo.append(temp)

    print(f'#{tc} {memo[N]}')
