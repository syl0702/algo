import sys
from pprint import pprint
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = list(map(int, input().split()))
    strings =[]
    result = []
    for char in range(N):
        
        strings.append(list(input()))

    for row in range(N):
        for col in range(N-M+1):
            for i in range(M//2):
                front = strings[row][col+i]
                back = strings[row][col+M-1-i]

                if front == back:
                    continue
                else:
                    break
            else:
                for j in range(M):
                    result.append(strings[row][col+j])

    for col in range(N):
        for row in range(N-M+1):
            for i in range(M//2):
                front = strings[row+i][col]
                back = strings[row+M-1-i][col]

                if front == back:
                    continue
                else:
                    break
            else:
                for j in range(M):
                    result.append(strings[row+j][col])

    print(result)
    answer = ''.join(result)
    print(answer)
    # pprint(strings)
    # string_list = []
    # reverse_list = []
    # for string in strings:
    #     # print(string)
    #     string_list.append(string[0:N//2])
    # # print(string_list)

    # for string in strings:
    #     reverse_list.append(list(reversed(string[(N//2):])))
    # # print(reverse_list)


    # for s in string_list:
    #     for r in reverse_list:
    #         if s == r:
    #             result = s +r
    #         else:
    #             continue
    # print(result)
