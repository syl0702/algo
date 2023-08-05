def solution(price):
    answer = 0
    temp = 0
    if price >= 500000:
        temp = price * 0.8
    elif price >= 300000:
        temp = price * 0.9
    elif price >= 100000:
        temp = price * 0.95
    else:
        temp = price
    answer = int(temp)
    return answer

print(solution(150000))
print(solution(580000))