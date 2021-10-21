def solution(left, right):
    answer = 0
    
    for i in range(left,right+1):   #13,14,15,16,17
        num =[]
        
        for j in range(1,i+1):   #1,2,...,13
            if i%j == 0:
                num.append(j)
                
        if len(num)%2 == 0:
            answer = answer+i
            print(num)
        else:
            answer = answer-i
            print(num)
                
    return answer
