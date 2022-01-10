def solution(n, arr1, arr2):
    answer = []

    for i in range(n):
        new_arr = bin(arr1[i] | arr2[i])
        new_arr = new_arr[2:].zfill(n)
        new_arr = new_arr.replace('1', '#').replace('0', ' ')
        answer.append(new_arr)

    return answer
