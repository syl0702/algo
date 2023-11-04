def solution(babbling):
    answer = 0
    for babble in babbling:
        result = 0
        word = ''
        for b in babble:
            word += b
            if word in ["aya", "ye", "woo", "ma"]:
               word = ''
               result += 1
        if len(word) == 0 and result > 0:
            answer += 1

    return answer

print(solution(["aya", "yee", "u", "maa"]))
print(solution(["ayaye", "uuu", "yeye", "yemawoo", "ayaayaa"]))