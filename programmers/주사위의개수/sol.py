def solution(box, n):
    answer = 0
    answer = (box[0] // n)*(box[1] // n)*(box[2] // n)
    return answer

print(solution([1, 1, 1], 1))
print(solution([10, 8, 6], 3))