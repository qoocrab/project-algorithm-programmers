# 예상 시간복잡도: O(K), K: 1까지의 인덱스
def solution(arr, idx):
    try:
        return arr[idx:].index(1) + idx
    except:
        return -1
    