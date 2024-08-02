def solution(elements):
    answer = 0
    # prefix_sum = [0]*len(elements) #누적합을 담을 배열
    # prefix_sum[0] = elements[0]
    # for i in range(1, len(elements)):
    #     prefix_sum[i] = prefix_sum[i-1] + elements[i]
    # elements.sort()
    # cache = [0] * len(elements)
    # cache[0] = elements[0]

    # 투포인터 알고리즘 공부해보자
    cnt = 0
    interval_sum = 0
    end = 0
    M = sum(elements)
    for start in range(len(elements)):
        while interval_sum < M and end < len(elements):
            interval_sum += elements[end]
            end += 1
        if interval_sum == M:
            cnt+= 1
        interval_sum -= elements[start]
    print(cnt)
    return answer

print(solution([7, 9, 1, 1, 4]))