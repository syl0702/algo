def solution(age):
    answer = ''
    temp = []
    t_a = []
    ages = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
    for n in str(age):
        temp.append(n)
    for i in range(0, len(temp)):
    
        answer += ages[int(temp[i])]
        
    return answer

print(solution(23))
print(solution(51))
print(solution(100))