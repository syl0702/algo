def solution(a, b):
    answer = 0
    for i in range(min(a, b), 0, -1):
        if a % i == 0 and b % i == 0:
            a = a // i
            b = b // i
            while b % 2 ==0:
                b //= 2
            while b % 5 == 0:
                b //= 5
            
            if b ==1:
                answer = 1
            else:
                answer = 2
    return answer
            

print(solution(7, 20))
print(solution(11, 22))
print(solution(12, 21))