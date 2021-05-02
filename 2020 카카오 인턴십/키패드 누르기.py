from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]


def solution(numbers, hand):
    data = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [-1, 0, -1]]
    ll, rl = [3, 0], [3, 2]
    answer = ""
    for i in numbers:
        if i in [1, 4, 7]:
            answer += "L"
            if i == 1:
                ll = [0, 0]
            elif i == 4:
                ll = [1, 0]
            else:
                ll = [2, 0]
        elif i in [2, 5, 8, 0]:
            q = deque()
            visited = [[0] * 3 for _ in range(4)]
            visited[ll[0]][ll[1]] = 1
            q.append(ll)
            while q:
                x, y = q.popleft()
                if data[x][y] == i:
                    lc = visited[x][y] - 1
                    break
                for d in range(4):
                    nx = x + dx[d]
                    ny = y + dy[d]
                    if 0 <= nx < 4 and 0 <= ny < 3:
                        if visited[nx][ny] == 0:
                            q.append([nx, ny])
                            visited[nx][ny] = visited[x][y] + 1

            q = deque()
            visited = [[0] * 3 for _ in range(4)]
            visited[rl[0]][rl[1]] = 1
            q.append(rl)
            while q:
                x, y = q.popleft()
                if data[x][y] == i:
                    rc = visited[x][y] - 1
                    break
                for d in range(4):
                    nx = x + dx[d]
                    ny = y + dy[d]
                    if 0 <= nx < 4 and 0 <= ny < 3:
                        if visited[nx][ny] == 0:
                            q.append([nx, ny])
                            visited[nx][ny] = visited[x][y] + 1

            if lc < rc:
                answer += "L"
                ch = 0
            elif lc > rc:
                answer += "R"
                ch = 1
            else:
                if hand == "left":
                    answer += "L"
                    ch = 0
                else:
                    answer += "R"
                    ch = 1
            if i == 2:
                if ch == 0:
                    ll = [0, 1]
                else:
                    rl = [0, 1]
            elif i == 5:
                if ch == 0:
                    ll = [1, 1]
                else:
                    rl = [1, 1]
            elif i == 8:
                if ch == 0:
                    ll = [2, 1]
                else:
                    rl = [2, 1]
            else:
                if ch == 0:
                    ll = [3, 1]
                else:
                    rl = [3, 1]
        elif i in [3, 6, 9]:
            answer += "R"
            if i == 3:
                rl = [0, 2]
            elif i == 6:
                rl = [1, 2]
            else:
                rl = [2, 2]
    return answer

numbers = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
hand = "right"
print(solution(numbers, hand))