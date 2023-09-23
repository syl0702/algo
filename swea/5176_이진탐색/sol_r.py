import sys
sys.stdin = open('input.txt')
T = int(input())

def intree(idx):
    global count
    if idx <= N:
        intree(idx*2)

        tree[idx] = count
        count += 1

        intree(idx*2 + 1)




for tc in range(1, T+1):
    N = int(input())
    tree = [0]*(N+1)

    count = 1

    intree(1)
    print(tree[1])
    print(tree[N//2])