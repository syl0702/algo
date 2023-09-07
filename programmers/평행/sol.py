def slope(dot1, dot2):
    return(abs((dot2[1]-dot1[1])/(dot2[0]-dot1[0])))


def solution(dots):
    answer = 0
    if slope(dots[0], dots[1]) == slope(dots[2], dots[3]):
        answer = 1
    if slope(dots[0], dots[2]) == slope(dots[1], dots[3]):
        answer = 1
    if slope(dots[0], dots[3]) == slope(dots[1], dots[2]):
        answer = 1


    return answer

print(solution([[1, 4], [9, 2], [3, 8], [11, 6]]))
print(solution([[3, 5], [4, 1], [2, 4], [5, 10]]))