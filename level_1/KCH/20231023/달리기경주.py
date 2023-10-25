# 예상 시간복잡도: O(N)
def solution(players, callings):
    status = {}
    for i in range(len(players)):
        status[players[i]] = i
    #status = {key: i for i, key in enumerate(players)}
        
    for name in callings:
        idx = status[name]
        players[idx], players[idx-1] = players[idx-1], players[idx]
        status[name] = idx-1
        status[players[idx]] = idx
        
    return players
