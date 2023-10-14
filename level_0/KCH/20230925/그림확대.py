# 예상 시간복잡도: O(NMk), M : picture[i] 길이 
def solution(picture, k):
    res = []
    for i in range(len(picture)):
        picture[i] = picture[i].replace('.','.'*k).replace('x','x'*k)
        res.extend([picture[i]] * k)
        
    return res
