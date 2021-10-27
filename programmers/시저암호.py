def caesar(s, n):
    s = list(s)
    for i in range(len(s)):
        if s[i].isupper():
            s[i]=chr((ord(s[i])-ord('A')+ n)%26+ord('A'))
        elif s[i].islower():
            s[i]=chr((ord(s[i])-ord('a')+ n)%26+ord('a'))
 
    return "".join(s)
 
print(caesar("a B z", 4)) # 'e F d'


# ord(c) : 문자의 아스키 코드값을 돌려주는 함수

# 66(B) - 65(A) + 1 %26 + 65(A)

