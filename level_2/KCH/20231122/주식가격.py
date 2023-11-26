# 예상 시간복잡도: O(NK), K : 슬라이스 길이
def solution(prices):
    res = []
    
    for i in range(len(prices)):
        for j in range(i, len(prices)):
            if prices[i] > prices[j]:
                res.append(j-i)
                break
        else:
            res.append(j-i)
                
    return res

# 예상 시간복잡도: O(N)
def solution(prices):
    stack = []
    answer = [0] * len(prices)
    for i in range(len(prices)):
        while stack != [] and stack[-1][1] > prices[i]: # 이전 가격중에 나보다 큰게 있으면 == 지금 떨어진 가격이 있으면
            past, _ = stack.pop() 
            answer[past] = i - past 
        stack.append([i, prices[i]]) # 인덱스, 가격
        
    for i, s in stack:
        answer[i] = len(prices) - 1 - i # 끝까지 안떨어진 가격은 여기서 처리
        
    return answer
