answer=0

def solution(num):
    global answer   #함수 안에서 전역변수 사용하기
    answer=answer+1  #재귀함수 호출 회수 세기

    if(num==1):
        return answer-1

    elif(answer<500):
        if(num%2==0):
            num=num//2
            return solution(num)  #재귀함수 사용

        else:
            num=num*3+1
            return solution(num)
    else:
        return -1
