def solution(n, words):
    answer = []
    temp = []
    for i in range(len(words)):
        if words[i] in temp:
            temp.append(words[i])
            answer.append((i+1)//n)
        else:
            i += 1

    return answer

print(solution(3, ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]))
print(solution(5, ["hello", "observe", "effect", "take", "either", "recognize", "encourage", "ensure", "establish", "hang", "gather", "refer", "reference", "estimate", "executive"]))
print(solution(2, ["hello", "one", "even", "never", "now", "world", "draw"]))