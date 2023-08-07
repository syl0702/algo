import sys
sys.stdin = open('input.txt')
T = int(input())

ways = [0, 1, 3]
def methods(N):
    
        
        for case in range(1, N+1):
            if case >= 2 and len(ways) <= case:
                print(ways, case, N)
                ways.append(methods(N-1) + methods(N-2)*2)
        
        return ways[N]

for tc in range(1, T+1):
    N = int(input()) // 10
    
        
    print(f'#{tc} {methods(N)}')
