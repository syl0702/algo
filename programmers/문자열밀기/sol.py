def solution(A, B):
    
    i = 0
    if A == B:
        return 0
    else:
        while i < len(A):
            i += 1
            A = A[-1] + A[:-1]
            if A == B:
                return i
    return -1

print(solution("hello", "ohell"))
print(solution("apple", "elppa"))
print(solution("atat", "tata"))
print(solution("abc", "abc"))