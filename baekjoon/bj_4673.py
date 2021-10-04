# 10000보다 작거나 같은 셀프넘버 출력


numbers = []
remove_list = []

# numbers[]에 10000까지 숫자를 넣어놓기
for i in range(1,10001,1):
    numbers.append(i)
    
for num in numbers:
    for j in str(num):
        #생성자 만들기
        num = num+int(j)

    #이렇게 해서 만들어진 수는 셀프넘버가 아님. 삭제될 숫자 리스트에 추가하기
    if num <= 10000:
        remove_list.append(num)


#remove_list 안에서 중복되는 숫자 지우고, numbers 리스트에서 빼기
#리스트-리스트 연산은 불가능. 덧셈만 가능
#집합으로 변경해서 빼준다.
self_numbers = set(numbers)-set(remove_list)

#숫자 순서대로 정렬해서 출력하기

for self_num in sorted(self_numbers):
    print(self_num) 
