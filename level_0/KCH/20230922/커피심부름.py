# 예상 시간복잡도: O(N)
def solution(order):
    res = 0
    order_dict = {
        "americano" : 4500,
        "cafelatte" : 5000,
        "anything" : 4500
    }
    
    for i in order:
        res += order_dict[i.replace('ice','').replace('hot','')]
        
    return res
