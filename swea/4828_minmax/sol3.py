import sys
sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    numbers = list(map(int, input().split()))
    answer = max(numbers) - min(numbers)
    print(f'#{tc} {answer}')

min_number = numbers[0]
max_number = numbers[0]

for number in numbers:
    if min_number > number:
        min_number = number
    
    if max_number < number:
        max_number = number

result = max_number - min_number