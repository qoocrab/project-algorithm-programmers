# 예상 시간복잡도: O(N)
def solution(n, words):
    already_ = dict()
    already_[words[0][0]] = [words[0]]
    
    for i in range(1,len(words)): 
        cur_first = words[i][0]
        ex_end = words[i-1][-1]
        
        if cur_first != ex_end:
            return [i%n+1, i//n +1]
            
        if cur_first in already_:
            if words[i] in already_[cur_first]:
                return [i%n+1, i//n +1]
            already_[cur_first].append(words[i])
        else:
            already_[cur_first] = [words[i]]
    return [0, 0]
