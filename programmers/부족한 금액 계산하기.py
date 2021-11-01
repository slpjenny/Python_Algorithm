def solution(price, money, count):
    price_result = 0

    for i in range(1,count+1):  #i=1,2,3,4
        price_result = price_result+price*i

    if money > price_result:
        answer=0
    else: 
        answer = price_result-money

    return answer
