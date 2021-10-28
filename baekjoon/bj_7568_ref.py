N = int(input())

student_list=[]

for _ in range(N):
    weight,height = map(int,input.split())
    student_list.append((weight,height))

#문제의 포인트는, 자기보다 무거운 사람을 구하면 되는 것!
for i in student_list:
    rank = 1
    for j in student_list:
        # 리스트에 들어있는 첫번째 학생부터 해당 학생이랑 몸무게와 키 둘 다 비교
        if i[0] < j[0] and i[1] < j[1]:
            rank += 1
            
    print(rank,end=" ")



#-----------2--------------------------
n = int(input())
 
li = []
# 변수저장
for i in range(n):
    li.append(list(map(int, input().split())))
 
# 덩치 비교
for i in range(n):
    rank = 1
    for j in range(n):
        if i!=j:
            if (li[i][0] < li[j][0]) and (li[i][1] < li[j][1]):
                rank +=1
    print(rank,end=' ')
