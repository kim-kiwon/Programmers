def solution(clothes):
    temp = {}
    for i in clothes:
        if i[1] in temp:
            temp[i[1]] += 1
        else:
            temp[i[1]] = 1
    answer = 1
    for i in temp.values():
        answer *= (i+1)
    return answer - 1