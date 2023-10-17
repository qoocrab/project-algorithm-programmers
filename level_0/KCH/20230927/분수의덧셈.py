# 예상 시간복잡도: O(N**2)
def solution(numer1, denom1, numer2, denom2):
    num_sum = numer1 * denom2 + numer2 * denom1
    dem_sum = denom1 * denom2
    for i in range(2,dem_sum):
        while dem_sum%i==0 and num_sum%i==0:
            dem_sum //= i
            num_sum //= i
        
    return [num_sum, dem_sum]

# cf) 유클리드 호제법 O(log(N))
def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a

def solution(numer1, denom1, numer2, denom2):
    num_sum = numer1 * denom2 + numer2 * denom1
    dem_sum = denom1 * denom2

    g = gcd(num_sum, dem_sum)
    return [num_sum//g, dem_sum//g]
