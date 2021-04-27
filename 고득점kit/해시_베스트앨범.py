from collections import Counter


def solution(genres, plays):
    g = dict()
    d = dict()

    for i in range(len(genres)):
        if genres[i] not in d:
            d[genres[i]] = plays[i]
        else:
            d[genres[i]] += plays[i]

        if genres[i] not in g:
            g[genres[i]] = [(plays[i], i)]
        else:
            g[genres[i]].append((plays[i], i))

    d = Counter.most_common(d)

    answer = []
    for i in d:
        now_gen = i[0]
        g[i[0]].sort(key=lambda x: (-x[0], x[1]))
        answer.append(g[i[0]][0][1])
        if len(g[i[0]]) == 1: continue
        answer.append(g[i[0]][1][1])

    return answer