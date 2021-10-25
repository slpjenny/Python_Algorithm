def solution(s):
    alp_dic = {'zero': 0, 'one': 1, "two": 2, "three": 3, "four": 4,
               "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}

    for i in alp_dic.keys():
        s = s.replace(i, str(alp_dic[i]))

    return int(s)
