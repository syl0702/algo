def solution(elements):
    answer = 0
    prefix_sum = [0]*len(elements) #누적합을 담을 배열
    prefix_sum[0] = elements[0]
    for i in range(1, len(elements)):
        prefix_sum[i] = prefix_sum[i-1] + elements[i]
        
    return answer

print([7, 9, 1, 1, 4])