def solution(n, words):
    answer = []
    temp = [] # 이미 사용된 단어 추적.
    temp.append(words[0])
    for j in range(1, len(words)):
        last_char = words[j-1][-1]
        first_char = words[j][0]

        if last_char == first_char and words[j] not in temp:
            temp.append(words[j])

        else:
            return [(j%n)+1, (j//n)+1]

        

    return [0, 0]

print(solution(3, ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]))
print(solution(5, ["hello", "observe", "effect", "take", "either", "recognize", "encourage", "ensure", "establish", "hang", "gather", "refer", "reference", "estimate", "executive"]))
print(solution(2, ["hello", "one", "even", "never", "now", "world", "draw"]))