# 예상 시간복잡도: O(N)
def solution(n):
    left, right, inter_sum = 1, 1, 1
    res = 0
    
    while left<=right:
        
        if inter_sum < n:
            right += 1
            inter_sum += right
        else:
            if inter_sum == n:
                res += 1
            inter_sum -= left
            left += 1
        
    return res 

## 투포인터 말고 2중 for문도 풀리긴 함
def solution(num):
    answer = 0
    for x in range(1,num+1):
        sum = 0
        for y in range(x, num+1):
            sum += y
            if sum == num:
                answer += 1
                break
            elif sum > num:
                break

    return answer
