# 예상 시간복잡도: O(N)
def solution(cipher, code):
    return ''.join([cipher[i] for i in range(code-1,len(cipher),code)])
