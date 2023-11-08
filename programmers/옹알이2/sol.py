import re
def solution(babbling):
    answer = 0
    for babble in babbling:
        result = 0
        if "aya" in babble:
            babble = babble.replace("aya", "*")
            
            babble_c = babble.count("*")
            if babble_c == 1:
                result += 1
        elif "ye" in babble:
            babble = babble.replace("ye","%")
            # babble_c = babble.count("%")
            # if babble_c == 1:
            #     result += 1
        
        elif "woo" in babble:
            babble = babble.replace("woo", "#")
            # babble_c = babble.count("#")
            # if babble_c == 1:
            #     result += 1
        
        elif "ma" in babble:
            babble = babble.replace("ma", "@")
            # babble_c = babble.count("@")
            # if babble_c == 1:
            #     result += 1
        

        # for b in babble:
        #     word += b
        #     if word in ["aya", "ye", "woo", "ma"]:
        #        word = ''
        #        result += 1
        # if len(word) == 0 and result > 0:
        #     answer += 1

    return answer

print(solution(["aya", "yee", "u", "maa"]))
print(solution(["ayaye", "uuu", "yeye", "yemawoo", "ayaayaa"]))