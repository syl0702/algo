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
    # cnt = 0
    # interval_sum = 0
    # end = 0
    # temp = []
    # M = sum(elements)
    # for start in range(len(elements)):
    #     while interval_sum < M and end < len(elements):
    #         interval_sum += elements[end]
    #         end += 1
    #         if interval_sum not in temp:
    #             temp.append(interval_sum)
    #             answer+= 1
    #         else:
    #             continue
    #     if interval_sum == M:
    #         answer+= 1
    #         interval_sum -= elements[start]
    # 원하는 답이 안 나온다...6이 한계!
    n = len(elements)
    elements = elements * 2 #for 원형배열 처리
    set_sums = set()

    for start in range(n):
        interval_sum = 0
        for length in range(1, n+1):
            interval_sum += elements[start+length-1]
            set_sums.add(interval_sum)
            answer = len(set_sums)
    return answer

print(solution([7, 9, 1, 1, 4]))