# 예상 시간복잡도: O(m) m : array length
def solution(array):
    tmp = array.copy()
    tmp.sort()
    max_value = tmp[len(tmp)-1]
    answer = [max_value,array.index(max_value)]
    return answer
