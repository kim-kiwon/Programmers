'''
세가지 연산문자만으로 이루어진 수식 전달.
연산자 우선순위 재정의해서 가장큰 숫자 제출.
+ - * 의 연산자 우선순위를 재정의하ㅏㅈ.
음수라면 절대값으로 변환.

'''
from copy import deepcopy
from itertools import permutations

def solution(expression):
    vals = set()
    operators = []
    count = 0
    for i in expression:
        if i == '*':
            operators.append([0, count])
            vals.add(0)
            count += 1
        elif i == '+':
            operators.append([1, count])
            vals.add(1)
            count += 1
        elif i == '-':
            operators.append([2, count])
            vals.add(2)
            count += 1

    vals = list(vals)
    choices = list(permutations(vals, len(vals)))

    answer = 0
    nums = list(map(int, expression.replace('-', '+').replace('*', '+').split('+')))
    for c in choices:  # 우선순위 별로 저장.
        t_nums = deepcopy(nums)
        t_operators = deepcopy(operators)
        for b in c:  # 우선순위 높은거부터
            for o in range(len(t_operators)):  # 오퍼레이터 저장된거에서 찾기
                if t_operators[o][0] == b:
                    if b == 0:
                        t_nums[t_operators[o][1]] *= t_nums[t_operators[o][1] + 1]
                    elif b == 1:
                        t_nums[t_operators[o][1]] += t_nums[t_operators[o][1] + 1]
                    elif b == 2:
                        t_nums[t_operators[o][1]] -= t_nums[t_operators[o][1] + 1]
                    del t_nums[t_operators[o][1] + 1]
                    for i in range(o, len(t_operators)):
                        t_operators[i][1] -= 1
        answer = max(answer, abs(t_nums[0]))
    return answer