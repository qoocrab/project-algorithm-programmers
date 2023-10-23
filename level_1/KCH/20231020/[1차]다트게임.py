# 예상 시간복잡도: O(N)
import re
def solution(dartResult):
    res, bonus = [], False
    area_dictionary = {'S':1, 'D':2, 'T':3}
    pattern = r'\d+[A-Z][*,#]?'
    for string in re.findall(pattern, dartResult):
        if string[-1] in ['#', '*']: 
            bonus = string[-1]
            string = string[:-1]
        num,area = int(string[:-1]), string[-1]
        
        res.append(num)
        res[-1] **= area_dictionary[area]

        if bonus == '*':
            res[max(-len(res),-2):] = [i*2 for i in res[max(-len(res),-2):]]
        elif bonus == '#': res[-1] *= -1
        bonus = False
    return sum(res)
