def solution(numlist, n):
    answer = sorted(numlist, reverse = True)
    answer = sorted(numlist, key = lambda x: (abs(n-x), n-x))

        
    return answer

print(solution([1, 2, 3, 4, 5, 6], 4))
print(solution([10000,20,36,47,40,6,10,7000], 30))