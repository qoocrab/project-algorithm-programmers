# 예상 시간복잡도: O(N)
def solution(myString, pat):
    for i in range(len(myString), -1, -1):
        if myString[:i][-len(pat):] == pat:
              return myString[:i]

# cf) rindex
# solution=lambda x,y:x[:x.rindex(y)+len(y)]
