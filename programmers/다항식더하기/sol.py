def solution(polynomial):
    x= 0
    n =0
    polynomial = polynomial.split(" + ")
    for num in polynomial:
        if num.isnumeric():
            n += int(num)
        else:
            if len(num) == 1:
                x+=1
            else:
                x+= int(num[:-1])
    x = str(x)
    n = str(n)
    if x == '0' and n == '0':
        return '0'
    if x == '0':
        return n
    if x == '1':
        x = ''
    if n == '0':
       return str(x) + 'x'
    return x + 'x + ' + n
    

print(solution("3x + 7 + x"))
print(solution("x + x + x"))