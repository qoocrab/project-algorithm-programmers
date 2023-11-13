# 예상 시간복잡도: O(nC2)
import itertools
def solution(numbers):
    res = []
    idx_list = list(range(len(numbers)))
    for idx1, idx2 in itertools.combinations(idx_list, 2):
        res.append(numbers[idx1] + numbers[idx2])
    return sorted(list(set(res)))

# 예상 시간복잡도: O(NlogN)
def solution(numbers):
    res = []
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            res.append(numbers[i] + numbers[j])
    return sorted(list(set(res)))
