def solution(spell, dic):
    answer = 0
    for d in dic:
        if sorted(d) == sorted(spell):
            return 1
        else:
            answer = 2
    return answer

print(solution(["p", "o", "s"], ["sod", "eocd", "qixm", "adio", "soo"]))
print(solution(["z", "d", "x"], ["def", "dww", "dzx", "loveaw"]))
print(solution(["s", "o", "m", "d"], ["moos", "dzx", "smm", "sunmmo", "som"]))