'''
배열형태에 다익스트라 사용.
distance : 그 곳 까지 가는데 최소비용.
'''

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
board = [[0, 0, 1, 0], [0, 0, 0, 0], [0, 1, 0, 1], [1, 0, 0, 0]]
import heapq
def solution(board):
    n = len(board)

    INF = int(1e9)
    distance = [[INF] * n for _ in range(n)]

    q = []
    q.append((0, 0, 0, -1))
    distance[0][0] = 0
    while q:
        x, y, dist, mode = heapq.heappop(q)
        if dist > distance[x][y]:
            continue
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if board[nx][ny] == 0:
                    if mode == -1 or (i % 2) == mode:
                        cost = dist + 100
                    else:
                        cost = dist + 600
                    if cost < distance[nx][ny]:
                        distance[nx][ny] = cost
                        heapq.heappush(q, ((nx, ny, cost, i % 2)))
                    elif cost == distance[nx][ny]: #비용 같아도 방향 다르게 왔을 수 있음 -> 다음 cost에 영향. 큐에 추가해주자.
                        heapq.heappush(q, ((nx, ny, cost, i % 2)))
    return distance

solution(board)