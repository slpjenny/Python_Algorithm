# n 번째 피보나치 수
n = int(input())

piv_list = [0,1]

def piv(N,pivList,i):
    if N == 0:
        return print(0)
    elif N == 1:
        return print(1)
    
    else:
        if i == N :
            return print(pivList[i])
        else:
            pivList.append(int(pivList[i])+int(pivList[i+1]))
            i=i+1

    piv(N,pivList,i)

piv(n,piv_list,0)
        
        


        
    
