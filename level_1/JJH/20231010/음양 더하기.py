# 에상 시간 복잡도 O(n) n absolutes length
def solution(absolutes, signs):
    answer = sum([absolutes[i] if signs[i] else -1 * absolutes[i] for i in range(0,len(absolutes))])
    return answer
