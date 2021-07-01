def solution(s):
    s= s.lower()
    
    countP= s.count('p')
    countY= s.count('y')
    
    if countP==countY :
        answer=True
    else:
        answer=False
    
    return answer
