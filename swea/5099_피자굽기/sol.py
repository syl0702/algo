import sys
from pprint import pprint
sys.stdin = open('input.txt')
T = int(input())

for tc in range(1, T+1):
    N, M = list(map(int, input().split()))
    numbers = list(map(int, input().split()))
    
    for cycle in range(max(numbers) // 2 + 1):
        for number in numbers:
            if number // 2 == 0:
                for i in numbers:
                    data = numbers.pop(number[i])
                    i = i + 1
                    numbers.append(data)
            
    print(numbers[-1])
