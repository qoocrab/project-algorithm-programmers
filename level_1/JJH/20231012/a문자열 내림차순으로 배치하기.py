# 예상 시간 복잡도 O(n^3/2 ~n^2) n is s length
def solution(s):
    sAsc = [ord(s[i]) for i in range(0, len(s))]
    sAsc.sort(reverse=True)
    answer = [chr(sAsc[i]) for i in range(0, len(s))]

    return ''.join(answer)

print(solution("Zbcdefg"))
