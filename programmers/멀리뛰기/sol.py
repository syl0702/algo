# def get_case_count(a, b):
#     if a == 0:
#         return 1
#     if a < b:
#         b = a
    
#     sum = 0

#     while b > 0:
#         sum += get_case_count(a - b, b)
#         b -= 1
#     return sum + 1

def solution(n):
    answer = 0
    cache = [0 for _ in range(n+2)]
    cache[1] = 1
    cache[2] = 2

    if n <= 2:
        answer += cache[n] % 1234567

    else:
        for i in range(3, n+1):
            cache[i] = cache[i-1] + cache[i-2]
            answer += cache[n] % 1234567
    return answer
    # 피보나치????
    # 합이 같은 부분집합?

    # while n > 0:
    #     if n > 2:
    #         temp.append(2)
    #         n = n-2
    #     elif n == 2:
    #         temp.append(2)
    #         n = n-2
    #     else:
    #         temp.append(1)
    #         n = n - 1
    # print(temp)

    # return answer

print(solution(4))
print(solution(3))