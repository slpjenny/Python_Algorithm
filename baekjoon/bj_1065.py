N = int(input())

# 100 보다 작으면 그자체로 무조건 등차수열이다
if N < 100:
    print(N)

else:
    # 해당 숫자가 등차수열이 맞으면 추가할 리스트
    hansu_list=[]

    
    # N만큼의 숫자 안에서 찾아야함. 반복하기
    for i in range(100,N+1,1):
        
        # 등차수열인지 확인할 용도의 리스트
        num_list = []
        
    
        for num in str(i):
            num_list.append(num)


        if len(num_list) < 4:
            if int(num_list[0])-int(num_list[1]) == int(num_list[1])-int(num_list[2]):
                # 등차수열 맞음
                hansu_list.append(int(i))
                
                
        else:
            if int(num_list[0])-int(num_list[1]) == int(num_list[1])-int(num_list[2]) == int(num_list[2])-int(num_list[3]):
                # 등차수열 맞음
                hansu_list.append(int(i))
        

    print(99+len(hansu_list))

        
