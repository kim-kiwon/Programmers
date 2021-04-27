from collections import Counter

def solution(participant, completion):
    temp = Counter(participant) - Counter(completion)
    temp = list(temp.keys())
    return temp[0]