# 예상 시간복잡도: O(N*logN)
## 10000까지의 소수
num = []
for i in range(2,10001):
    for j in range(2,i):
        if i%j==0:
            break
    else:
        num.append(i)

def divide(n, i):
    while n%i==0:
        n//=i
    return n
    
    
def solution(n):
    global num
    res = []
    for i in num:
        if n%i == 0:
            res.append(i)
            n = divide(n, i)
    return res

## cf) O(N*K), K: answer 길이
# def solution(n):
#     answer = []
#     d = 2
#     while d <= n:
#         if n % d == 0:
#             n /= d
#             if d not in answer:
#                 answer.append(d)
#         else:
#             d += 1
#     return answer
