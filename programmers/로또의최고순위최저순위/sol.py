def winrank(nums):
    if nums == 6:
        result = 1
    elif nums == 5:
        result = 2
    elif nums == 4:
        result = 3
    elif nums == 3:
        result = 4
    elif nums == 2:
        result = 5
    else:
        result = 6
    return result

def solution(lottos, win_nums):
    answer = []
    temp = []
    win_rank = {1:6, 2:5, 3:4, 4:3, 5:2}
    # 0 그냥 무시하고 있는 상태로만 갯수 세기 (min)
    count_min = 0
    for l in lottos:
        if l in win_nums:
            count_min += 1
        
    answer.append(winrank(count_min))


    # 당첨 번호에 구매 로또가 있다면 빼기
    lottos.sort()
    win_nums.sort()
    for num in win_nums:
        if num not in lottos:
            temp.append(num)
    # print(temp)

    

    # 구매한 로또에 0이 있다면 temp 중 몇개를 지정하기 (max)
    for j in range(len(lottos)):
        if lottos[j] == 0:
            lottos[j] += temp[j]
                
    # print(lottos)



    # 구매한 로또와 당첨 번호 비교하기
    count_max = 0
    for l in lottos:
        
        if l in win_nums:
            count_max += 1
        
    answer.append(winrank(count_max))

    answer.reverse()
    return answer

print(solution([44, 1, 0, 0, 31, 25], [31, 10, 45, 1, 6, 19]))
print(solution([0, 0, 0, 0, 0, 0], [38, 19, 20, 40, 15, 25]))
print(solution([45, 4, 35, 20, 3, 9], [20, 9, 3, 45, 4, 35]))