# 예상 시간복잡도: O(N)
def solution(myStr):
    res = myStr.replace('a',' ').replace('b',' ').replace('c',' ').split()
    return res if res else ["EMPTY"]

# cf) re
# import re
# def solution(myStr):
#     answer = [m for m in re.split('a|b|c',myStr) if m]
#     if len(answer)==0:
#         answer=["EMPTY"]

#     return answer
