s = input()

# 문자열의 모든 알파벳을 대문자로 바꾸기
s = s.upper()

a_set=set()
for i in s:
    a_set.add(i)

a_dic={}

for j in list(a_set):
    # 각 알파벳이 몇개 속해있는지 세어서 딕셔너리로 만듬
    a_dic[j]=s.count(j)

# 최대 value에 대한 key 찾기
# .get -> 해당 key에 f대한 value 출력

max(a_dic, key=a_dic.get)

answer = [k for k,v in a_dic.items() if max(a_dic.values()) == v]


# value의 최대값에 대한 모든 key 출력
if len(answer) >= 2:
    print('?')
else:
    print("".join(answer))
