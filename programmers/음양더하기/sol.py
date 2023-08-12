def solution(absolutes, signs):
    answer = 0
    temp = zip(signs, absolutes)
    temp_list = list(temp)
    final = []
    for i in range(len(temp_list)):
        
        if temp_list[i][0] == False:
            
            j = list(temp_list[i])
            j[1] = -j[1]
            temp_list[i] = tuple(j)
            # print(temp_list) [(True, 4), (False, -7), (True, 12)]
    for k in range(len(absolutes)):      
        final.append(temp_list[k][1])
        answer = sum(final)
    
    return answer

print(solution([4,7,12], [True,False,True]))
print(solution([1, 2, 3], [False, False, True]))