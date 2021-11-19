def solution(n):
    answer = 0
    namugi = []
    samjin = 0

    while(n > 0):
        namugi.append(n % 3)  # 0021 순서대로 리스트에 넣기
        n = n//3

    namugi.reverse()  # reverse() 함수는 iterable 객체로 반환한다

    # 0021 을 10진법으로 다시 바꾸기
    for i in namugi:
        answer = answer + 3**samjin * i  # 3의 제곱수를 곱하며 더하기
        samjin += 1

    return answer
