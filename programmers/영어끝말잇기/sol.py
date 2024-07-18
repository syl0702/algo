def solution(n, words):
    answer = []
    temp = []
    for j in range(len(words)-1):
        last_char = words[j][-1]
        first_char = words[j+1][0]
        if last_char == first_char:
            for i in range(len(words)):
                if words[i] in temp:
                    temp.append(words[i])
                    answer.append((i+1)//n)
                    break
        
                else:
                    temp.append(words[i])
                    i += 1
                    continue
        else:
            answer.append((j+1)//n)
            break

    return answer

print(solution(3, ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]))
print(solution(5, ["hello", "observe", "effect", "take", "either", "recognize", "encourage", "ensure", "establish", "hang", "gather", "refer", "reference", "estimate", "executive"]))
print(solution(2, ["hello", "one", "even", "never", "now", "world", "draw"]))