import sys
sys.stdin = open('input.txt')
T = int(input())

for tc in range(1, T+1):
    E, N = list(map(int, input().split()))

    for i in range(1, E+1):
        print()