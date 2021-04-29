from collections import deque
from collections import Counter

def solution(begin, target, words):
    q = deque()
    q.append((begin, 0))
    visited = [0] * len(words)
    while q:
        now, count = q.popleft()
        if now == target: return count
        a = Counter(now)
        for i in range(len(words)):
            b = Counter(words[i])
            c = a - b
            c_tem = list(c.items())
            if len(c_tem) == 1 and c_tem[0][1] == 1 and visited[i] == 0:
                q.append((words[i], count + 1))
                visited[i] = 1
    return 0