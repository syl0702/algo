import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1,T+1):
    N= int(input())
    numbers = list(map(int, input().split()))

    min_number = numbers[0]
    max_number = numbers[0]

    for num in numbers:
        if min_number > num:
            min_number = num
        if max_number < num:
            max_number = num
    
result = max_number - min_number


print(f'#{tc} {result}')
