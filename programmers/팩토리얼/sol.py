def n_factorial(i):
    if (i>1):
        return i * n_factorial(i-1)
    else:
        return 1

def solution(n):
    answer = 0
    temp= []
    for num in range(n+1):
        if n_factorial(num) <= n:
            temp.append(num)
            answer = max(temp)
        else:
            break
    return answer

print(solution(3628800))
print(solution(7))