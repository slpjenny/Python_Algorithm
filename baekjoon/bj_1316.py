# 단어의 개수 N
N = int(input())

word=[]

group_word=[]

# 단어들을 한 리스트에 추가함
for i in range(N):
    word.append(i)

# 단어 리스트를 돌면서, '그룹 단어' 인지 체크
for j in word:
    print(j)
    # 처음에 받은 단어 순서대로 출력
