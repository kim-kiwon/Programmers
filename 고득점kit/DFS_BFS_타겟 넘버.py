'''
n개의 음이 아닌 정수.
이를 더하고 빼서 목표 수를 만들자.
만드는 방법 수 반환.
'''

answer = 0
def dfs(now, count, numbers, target):
    global answer
    if count == len(numbers):
        if now == target:
            answer += 1
        return
    dfs(now + numbers[count], count + 1, numbers, target)
    dfs(now - numbers[count], count + 1, numbers, target)

def solution(numbers, target):
    global answer
    dfs(0, 0, numbers, target)
    return answer