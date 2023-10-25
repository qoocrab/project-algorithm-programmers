# 예상 시간복잡도: O(N)
def solution(today, terms, privacies):
    res = []
    term_dict = {}
    
    for term in terms:
        t, d = term.split()
        term_dict[t] = d
        
    for i in range(len(privacies)):
        date, p_type = privacies[i].split()
        if date_diff(date, int(term_dict[p_type]), today):
            res.append(i+1)
            
    return res

def date_diff(date, month, today):
    y1, m1, d1 = list(map(int,date.split('.')))
    y2, m2, d2 = list(map(int,today.split('.')))
    
    m1 += month
    if m1 > 12:
        y1 += 1
        m1 -= 12
        
    tmp = (y2-y1) * (28*12) + (m2 - m1) * 28 + d2 - d1
    return int(tmp >= 0)
