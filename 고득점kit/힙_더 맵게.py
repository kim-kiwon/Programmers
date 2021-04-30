import heapq

def solution(scoville, K):
    q = []
    for i in scoville:
        heapq.heappush(q, i)
    count = 0
    while True:
        if len(q) == 1: break
        a = heapq.heappop(q)
        if a >= K:
            break
        b = heapq.heappop(q)
        val = a + (b * 2)
        heapq.heappush(q, val)
        count += 1
    if q[0] < K: return -1
    else: return count