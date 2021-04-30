'''
백트래킹 활용
매개변수 리스트인 countries에 추가시. 다음 경우의수인 다른 for문에서 영향주는 것에 조심.
'''

data = []

def dfs(visited, tickets, countries, a):
    if visited.count(0) == 0:
        data.append(countries + [tickets[a][1]])
        return
    for i in range(len(tickets)):
        if tickets[i][0] == tickets[a][1] and visited[i] == 0:
            visited[i] = 1
            dfs(visited, tickets, countries + [tickets[i][0]], i)
            visited[i] = 0


def solution(tickets):
    visited = [0] * len(tickets)
    for i in range(len(tickets)):
        if tickets[i][0] == "ICN":
            visited[i] = 1
            dfs(visited, tickets, [tickets[i][0]], i)
            visited[i] = 0
    data.sort()
    return data[0]