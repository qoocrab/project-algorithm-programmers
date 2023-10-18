def solution(nums):
    answer = 0
    list = [0 for i in range(0,max(nums)+1)]
    typeNum = 0
    for i in nums:
        if list[i] == 0:
            typeNum = typeNum + 1
        list[i] = list[i] + 1

    if typeNum < len(nums) // 2:
        answer = typeNum
    else:
        answer = len(nums)//2

    return answer
