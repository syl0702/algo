def solution(n, words):
    answer = []
    temp = set() # 이미 사용된 단어 추적.
    temp.add(words[0])
    for j in range(len(words)-1):
        if j > 0:
            last_char = words[j][-1]
            first_char = words[j+1][0]
        
            if last_char != first_char:
                answer = [(j % n)+1, (j//n)+1]
                break

    # 단어 중복 체크
        if words[j] in temp:
            answer = [(j % n)+1, (j//n)+1]
            break


        temp.add(words[j])
        
    else:
        answer = [0, 0]

    return answer

print(solution(3, ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]))
print(solution(5, ["hello", "observe", "effect", "take", "either", "recognize", "encourage", "ensure", "establish", "hang", "gather", "refer", "reference", "estimate", "executive"]))
print(solution(2, ["hello", "one", "even", "never", "now", "world", "draw"]))