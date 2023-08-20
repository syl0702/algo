from pprint import pprint
def solution(n, arr1, arr2):
    
    temp = []
    temp2 = []
    # temp = list(map(bin, arr1))
    answer = [['0'] * (n) for _ in range(n)]
    result = []

    for a in arr1:
        a = format(a, 'b')
        a = a.zfill(n)
        temp.append(list(a))
    
    # pprint(temp)
        

    for b in arr2:
        b = format(b, 'b')
        b = b.zfill(n)
        temp2.append(list(b))

    # pprint(temp2)
    
    for i in range(n):
        for j in range(n):
            if temp[i][j] == '1' and temp2[i][j] == '1':
                k = answer[i][j].replace('0', '#')
                result.append(k)
            elif temp[i][j] == '1' and temp2[i][j] == '0':
                k = answer[i][j].replace('0', '#')
                result.append(k)
            elif temp[i][j] == '0' and temp2[i][j] == '1':
                k = answer[i][j].replace('0', '#')
                result.append(k)
            elif temp[i][j] == '0' and temp2[i][j] == '0':
                k = answer[i][j].replace('0', ' ')
                result.append(k)
    result = [result[f * n:(f+1)*n] for f in range((len(result) + n-1) //n)]
    # print(type(result[0]))
    final = []
    for _ in range(0, n):
        final.append(''.join(result[_]))
    return final

print(solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28]))
print(solution(6, [46, 33, 33 ,22, 31, 50], [27 ,56, 19, 14, 14, 10]))