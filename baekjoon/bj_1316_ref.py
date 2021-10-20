N = int(input())

#그룹단어 개수 변수
group_word=0

for _ in range(N):
    word=input()
    error=0

    for index in range(len(word)-1):
        if word[index] != word[index+1]:  
            new_word = word[index+1:]  #현재글자이후 새로운 문자를 단어로 생성
            if new_word.count(word[index])>0:
                    error = error+1

    if error == 0 :
        group_word += 1

print(group_word)            
            
