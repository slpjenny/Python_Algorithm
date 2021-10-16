word = str(input())

croatia_alp = ['c=','c-','dz=','d-','lj','nj','s=','z=']


for i in croatia_alp:
    word = word.replace(i,"*")


print(len(word))
        

