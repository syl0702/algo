import sys
sys.stdin = open('input.txt', encoding = 'utf-8')

Man1 = input()
Man2 = input()

if Man1 == '바위' and Man2 == '바위':
    print('Result : Draw')
elif Man1 == '바위' and Man2 == '가위':
    print('Result : Man1 Win!')
elif Man1 == '바위' and Man2 == '보':
    print('Result : Man2 Win!')
elif Man1 == '가위' and Man2 == '가위':
    print('Result : Draw')
elif Man1 == '가위' and Man2 == '보':
    print('Result : Man1 Win!')
elif Man1 == '가위' and Man2 == '바위':
    print('Result : Man2 Win!')

elif Man1 == '보' and Man2 == '보':
    print('Result : Draw')
elif Man1 == '보' and Man2 == '바위':
    print('Result : Man1 Win!')
elif Man1 == '보' and Man2 == '가위':
    print('Result : Man2 Win!')