# 예상 시간복잡도: O(N**2,,)
def solution(arr):
    i = 1
    MAX = max(arr)
    while True:
        for num in arr:
            if ((MAX * i)%num) != 0:
                break
        else: return MAX*i
        i += 1

# gcd와 lcm 
# def gcd(a, b):
#     if b == 0:
#         return a
#     return gcd(b, a%b)

# def nlcm(num):
#     num.sort()
#     temp = 1
#     for i in range(len(num)):
#         temp = (num[i] * temp) / (gcd(num[i], temp))
#     return temp
