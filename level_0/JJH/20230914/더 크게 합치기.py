# 예상 시간복잡도: O(1)
def solution(a, b):
    answer = 0
    a_b = ''.join([str(a),str(b)])
    b_a = ''.join([str(b),str(a)])
    if int(a_b) > int(b_a):
        answer = int(a_b)
    else:
        answer = int(b_a)
    return answer
