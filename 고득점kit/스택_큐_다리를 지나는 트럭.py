from collections import deque

def solution(bridge_length, weight, truck_weights):
    truck_weights.reverse()
    now = deque()
    count = 0
    time = 0
    truck_count = len(truck_weights)
    now_weight = 0
    
    while count < truck_count:
        if now:
            for i in now:
                i[0] -= 1
    
        rm_count = 0
        if now:
            for i in now:
                if i[0] >0: break
                rm_count += 1

        for i in range(rm_count):
            a = now.popleft()
            now_weight -= a[1]
            count += 1
        
        if truck_weights and now_weight + truck_weights[-1] <= weight:
            a = truck_weights.pop()
            now.append([bridge_length, a])
            now_weight += a

        time += 1
    return time