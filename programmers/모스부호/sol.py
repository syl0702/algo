def solution(letter):
    answer = ''
    morse = { 
    '.-':'a','-...':'b','-.-.':'c','-..':'d','.':'e','..-.':'f',
    '--.':'g','....':'h','..':'i','.---':'j','-.-':'k','.-..':'l',
    '--':'m','-.':'n','---':'o','.--.':'p','--.-':'q','.-.':'r',
    '...':'s','-':'t','..-':'u','...-':'v','.--':'w','-..-':'x',
    '-.--':'y','--..':'z'
}
    # print(type(letter))
    
    temp = letter.split(' ')
    # print(temp)
    # print(type(temp))
    
    # print(morse.keys())
    for i in range(len(temp)):
        for key in list(morse.keys()):
            if temp [i] == key :
                answer += morse[key]
    return answer

print(solution(".... . .-.. .-.. ---"))
print(solution(".--. -.-- - .... --- -."))