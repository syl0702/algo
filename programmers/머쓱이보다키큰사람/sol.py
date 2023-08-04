def solution(array, height):
    answer = 0
    
    for ppl in array:
        if ppl > height:
            answer += 1
        else:
            pass

        
    return answer

print(solution([149, 180, 192, 170], 167))
print(solution([180, 120, 140], 190))