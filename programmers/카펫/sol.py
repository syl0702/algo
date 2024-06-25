def solution(brown, yellow):
    answer = []
    sums = brown + yellow
    for i in range(1, sums):
        if sums % i == 0:
            pairs = sums // i
            if abs(pairs-i) <= 2:
                answer = [i, pairs]
                answer.sort(reverse=True)
    return answer

print(solution(10, 2))
print(solution(8, 1))
print(solution(24, 24))