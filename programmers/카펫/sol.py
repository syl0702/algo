def solution(brown, yellow):
    answer = []
    # mins = float('inf')
    # sums = brown + yellow
    # for i in range(1, sums//2):
    #     if sums % i == 0:
    #         pairs = sums // i
    #         diff = abs(pairs-i)
    #         if diff < mins:
    #             mins = diff
    #             answer = [i, pairs]
    # answer.sort(reverse=True)
    # 76.9% 정답률이 최대

    # 2nd solution
    sums = brown + yellow
    for bh in range(1, brown//2+1):
        bw = (brown - 2*bh+4) //2
        yw, yh = bw-2, bh-2
        if yellow == yw * yh and sums == bw*bh:
            answer = [bh, bw]
    
    return answer


print(solution(10, 2))
print(solution(8, 1))
print(solution(24, 24))
print(solution(50, 22))