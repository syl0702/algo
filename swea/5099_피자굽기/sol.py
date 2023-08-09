import sys
from pprint import pprint
sys.stdin = open('input.txt')
T = int(input())

for tc in range(1, T+1):
    # N : 화덕의 크기
    # M : 피자 개수
    N, M = list(map(int, input().split()))

    Ci = list(map(int, input().split()))
    
    # 피자에 번호를 부여하는 과정
    # 화덕에 들어가기 전 세팅만 되어진 피자
    before = []
    for i in range(M):
        before.append([Ci[i], i])
    
    # 화덕
    queue = [0] * N

    # 완성 피자를 저장할 목록
    after = []

    # 완성 피자가 구워야 하는 피자 갯수랑 같아질 때까지 반복
    while len(after) != M:

        # 화덕 입구에 공간이 비었으면
        if queue [0] == 0:
            # 넣을 피자가 있으면
            if len(before) != 0:
                # 남은 첫번째 치즈와 번호
                cheese, idx = before.pop(0)
                # 화덕에 넣기
                queue.append([cheese, idx])
                # 화덕 돌리기
                queue.pop(0)
            # 넣을 피자가 없을 때
            else:
                queue.pop(0)
                queue.append(0)      

        # 화덕 입구에 공간이 없으면 (이미 구워지고 있는 피자가 있는 경우)
        else:
            # 치즈 절반 감소
            queue[0][0] //= 2

            # 치즈가 다 녹았는지 확인
            if queue[0][0] == 0:
                # 완성된 피자 꺼내기
                pizza = queue.pop(0)
                # 완성 목록에 넣기
                after.append(pizza)

                if len(before) != 0:
                    # 남은 첫번째 치즈와 번호
                    cheese, idx = before.pop(0)
                    # 화덕에 넣기
                    queue.append([cheese, idx])
                # 넣을 피자가 없으면비어있는 판 추가
                else:
                    queue.append(0)
            # 아직 더 돌려야 하는 경우
            else:
                queue.append(queue.pop(0))
    
    print(after)