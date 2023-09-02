import sys
from pprint import pprint
sys.stdin = open('input.txt')
T = int(input())

for tc in range(1, T+1):
    N = int(input())
    numbers = list(map(int, input().split()))
    
    result = []
    temp = []
    # print(numbers)
    for i in range(N//2):
        temp = [max(numbers), min(numbers)]
        
        result.append(temp)
        # print(result)
        # print(numbers)
        numbers.remove(temp[0])
        numbers.remove(temp[-1])
    # print(numbers)
    answer = sum(result, [])
    print(answer)

