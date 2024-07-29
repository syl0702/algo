from collections import Counter
def solution(k, tangerine):
    answer = 0
    value_s = 0
    # dictionary 형태로 각 숫자가 몇개 나오는지 파악하기
    tangs = Counter(tangerine)
    # print(tangs)
    # print(tangs.most_common(1))
    # print(tangs.elements())
    # print(tangs.items())
    # print(tangs.keys())
    # print(tangs.values())
    sorted_t = tangs.most_common()
    # print(sorted_t)
    # 최대한 심플하게 하는 것을 목표로 해볼 것!
    for key, value in sorted_t:
        if value_s < k:
            answer += 1
            value_s += value
        else:
            break # value_s가 k 이상이면 루프 종료
            
    return answer

print(solution(6, [1, 3, 2, 5, 4, 5, 2, 3]))
print(solution(4, [1, 3, 2, 5, 4, 5, 2, 3]))
print(solution(2, [1, 1, 1, 1, 2, 2, 2, 3]))