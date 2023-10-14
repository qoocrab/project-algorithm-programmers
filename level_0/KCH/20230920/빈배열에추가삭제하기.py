# 예상 시간복잡도: O(N*K), K: 삭제하는 길이..
def solution(arr, flag):
    res = []
    for f in range(len(flag)):
        if flag[f]:
            res += [arr[f]] * arr[f]*2
        else:
            res = res[:-arr[f]]
    return res
