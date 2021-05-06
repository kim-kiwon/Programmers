'''
해시의 탐색 및 deque의 popleft 활용 ==> 둘 다 O(1)
시간복잡도 최소화
'''
n = 9
path = 	[[0,1],[0,3],[0,7],[8,1],[3,6],[1,2],[4,7],[7,5]]
order = [[8,5],[6,7],[4,1]]

def solution(n, path, order):
    from collections import deque

    adj = {n: [] for n in range(n)}
    for a, b in path:
        adj[a].append(b)
        adj[b].append(a)

    check1 = {}
    check2 = {}
    for a, b in order:
        if b == 0: return False
        check1[a] = b  # a 가야 b 가능
        check2[b] = a  # b는 a가야 가능

    visited = [0 for _ in range(n)]
    q = deque()
    q.append(0)
    visited[0] = 1

    while q:
        val = q.popleft()
        for i in adj[val]:
            if visited[i] != 0:
                continue
            if i in check2 and visited[check2[i]] != 1:
                visited[i] = 2
                continue
            q.append(i)
            visited[i] = 1
            if i in check1 and visited[check1[i]] == 2:
                q.append(check1[i])
                visited[check1[i]] = 1
    if visited.count(1) == n:
        return True
    else:
        return False

print(solution(n,path,order))