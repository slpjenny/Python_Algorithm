def solution(s):
    s=list(s)     #입력받은 문자열을 리스트로 변환
    s.sort(reverse=True)      #리스트를 역순으로 정렬
    return "".join(s)         # 다시 문자열로 바꾸어 출력
