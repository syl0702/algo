from collections import Counter
def solution(k, tangerine):
    answer = 0
    # dictionary 형태로 각 숫자가 몇개 나오는지 파악하기
    tangs = Counter(tangerine)
    print(tangs)
    print(tangs.most_common(1))
    print(tangs.elements)
    return answer

print(solution(6, [1, 3, 2, 5, 4, 5, 2, 3]))
print(solution(4, [1, 3, 2, 5, 4, 5, 2, 3]))
print(solution(2, [1, 1, 1, 1, 2, 2, 2, 3]))