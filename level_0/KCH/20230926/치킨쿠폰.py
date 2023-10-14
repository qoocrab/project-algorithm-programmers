 # 예상 시간복잡도: O(N)
def solution(chicken):
    total, res = 0, 0
    while chicken:
        res += chicken%10
        chicken //= 10
        total += chicken
        if res//10:
            total += res//10
            chicken += res//10
            res %=10
        
    return total + res//10

# cf) int(chicken*0.11111111111)
# cf) (max(chicken,1)-1)//9
# cf)
'''
def solution(chicken):
    output = 0

    while chicken >= 10:
        output += chicken // 10
        chicken = chicken // 10 + chicken % 10

    return output
'''
