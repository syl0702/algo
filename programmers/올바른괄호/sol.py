def solution(s):
    answer = True
    if s[0] == ")":
        return False
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    print('Hello Python')

    return True

print(solution("()()"))
print(solution("(())()"))
print(solution(")()("))
print(solution("(()("))