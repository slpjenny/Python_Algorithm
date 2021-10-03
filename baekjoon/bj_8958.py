testN = int(input())

for i in range(testN):
    array = list(str(input()))

    score = 0
    scoreSum = 0

    for j in array:
        if j == 'O':
            score = score+1
            scoreSum = scoreSum +score

        elif j == 'X':
            score = 0

    print(scoreSum)

  
