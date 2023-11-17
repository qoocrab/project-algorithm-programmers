# 예상 시간복잡도: O(N**2)
def solution(elements):
    elements+=elements
    res = set()
    
    # for i in range(1, len(elements)//2 + 1):
        # for s in range(len(elements)-i):
            # res.add(sum(elements[s:s+i]))
         
    for i in range(len(elements)//2):
        summ = 0
        for j in range(len(elements)//2):
            summ += elements[i+j]
            res.add(summ)
            
    return len(res)
