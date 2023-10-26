
def solution(ingredient):
    cnt = 0
    ing_str = ''.join(list(map(str,ingredient)))
    while idx:=(ing_str.find('1231')+1):
        if idx<1: break
        idx -= 1
        cnt += 1
        ing_str = ing_str[:idx] + ing_str[idx+4:]

    return cnt
