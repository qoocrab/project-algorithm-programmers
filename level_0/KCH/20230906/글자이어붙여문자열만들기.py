# 예상 시간복잡도: O(N)
def solution(my_string, index_list):
    ans = ''
    for idx in index_list:
        ans += my_string[idx]
    return ans
