import sys
sys.stdin = open('input.txt', encoding='utf-8')

Man1 = input() # 바위
Man2 = input() # 가위

rcp = ['가위', '바위', '보']

Man1_idx = rcp.index(Man1)
Man2_idx = rcp.index(Man2)

result = Man1_idx - Man2_idx

if result == 0:
    print('Result : Draw')
elif result > 0:
    print(f'Result : Man{result} Win!')
else:
    if result == -1:
        print('Result : Man2 Win!')
    else:
        print('Result : Man1 Win!')

# 가위, 바위, 보
# 0        1   2





# if Man1 == '가위' and Man2 == '가위':
#     print('Result : Draw')
# elif Man1 == '가위' and Man2 == '바위':
#     print('Result : Man2 Win!')
# elif Man1 == '가위' and Man2 == '보':
#     print('Result : Man1 Win!')

# Man1 = input()
# Man2 = input()

# def compare(Man1, Man2):
#     if Man1 == Man2:
#         print('Result : Draw')
#     elif Man1 == '바위':
#         if Man2 == '가위':
#             print('Result : Man1 Win!')
#         else:
#             print('Result : Man2 Win!')    

#     elif Man1 == '가위':
#         if Man2 == '보':
#             print('Result : Man1 Win!')
#         else:
#             print('Result : Man2 Win!')

#     elif Man1 == '보':
#         if Man2 == '주먹':
#             print('Result : Man1 Win!')
#         else:
#             print('Result : Man2 Win!')
