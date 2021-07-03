def solution(s):
    a=len(s)//2
    
    if len(s)%2 == 1:             #s 길이가 홀수일 때
        return s[a]
    else:                         #s 길이가 짝수일 때
        return s[a-1]+s[a]
