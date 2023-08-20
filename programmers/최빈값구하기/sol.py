def solution(array):
    answer = 0
    array1 = list(set(array))
    temp = []
    temp1= 0
    for a in array1:
        temp.append(array.count(a))
    a_dict = {idx: counts for idx, counts in zip(array1, temp)}
    # max_array = max(a_dict, key=a_dict.get)
    temp1 = [k for k,v in a_dict.items() if max(a_dict.values()) == v]
    if len(temp1) > 1:
        answer = -1
    elif len(temp1) == 1:
        answer = temp1[0]
    return answer

print(solution([1, 2, 3, 3, 3, 4]))
print(solution([1, 1, 2, 2]))
print(solution([1]))