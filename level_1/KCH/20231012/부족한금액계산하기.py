# 예상 시간복잡도: O(N)
def solution(price, money, count):
    res = price*sum(list(range(1, count+1))) - money
    return max(res, 0)

# 등차수열의 합
# (count+1)*count//2
