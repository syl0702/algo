def solution(brown, yellow):
    answer = []
    mins = float('inf')
    sums = brown + yellow
    for i in range(1, sums):
        if sums % i == 0:
            pairs = sums // i
            diff = abs(pairs-i)
            if diff < mins:
                mins = diff
                answer = [i, pairs]
            
    answer.sort(reverse=True)        

            # answer = mins
            # answer.sort(reverse=True)
            # if abs(pairs-i) <= 2:
            #     answer = [i, pairs]
            #     answer.sort(reverse=True)
            
    return answer

print(solution(10, 2))
print(solution(8, 1))
print(solution(24, 24))