# 예상 시간 복잡도 O(n)
def solution(number, limit, power):
    answer = 0
    weaponList = [getWeapon(i) if getWeapon(i) <= limit else power for i in range(1,number+1)]
    return sum(weaponList)

def getWeapon(level):
    result = 0
    for i in range(1,int(level**(1/2))+1):
        if level % i == 0:
            if i**2 == level:
                result += 1
            else:
                result += 2
    return result
