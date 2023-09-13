# 예상 시간복잡도: O(m) m : string length
def solution(cipher, code):
    answer = ''.join(cipher[i] for i in range(code-1,len(cipher),code))
    return answer
