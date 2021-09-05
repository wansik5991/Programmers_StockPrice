import os
def solution(prices):
    answer = list(len(prices)-1-i for i in range(len(prices)))
    result = []
    for ind in range(len(prices)) :
        while result and prices[ind] < prices[result[-1]] :
            answer[result[-1]] = ind - result[-1]
            result.pop()
        result.append(ind)
    return answer

os.system('cls')
print('정답 : ',solution([1,2,3,2,3]))
print('정답 : ',solution([1,2,3,2,3,2,1,2,1]))