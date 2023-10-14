# 예상 시간복잡도: O(N)
def solution(numbers):
    number_dict = {
        "zero" : '0',
        "one" : '1',
        "two" : '2',
        "three" : '3',
        "four" : '4',
        "five" : '5',
        "six" : '6',
        "seven" : '7',
        "eight" : '8',
        "nine" : '9' 
    }
    res = ''
    idx = 0
    while numbers:=numbers[idx:]:
        idx = 0
        if numbers[:3] in number_dict:
            res += number_dict[numbers[:3]]
            idx = 3
        elif numbers[:4] in number_dict:
            res += number_dict[numbers[:4]]
            idx = 4
        elif numbers[:5] in number_dict:
            res += number_dict[numbers[:5]]
            idx = 5
            
    return int(res)

# cf)
# def solution(numbers):
#     for num, eng in enumerate(["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]):
#         numbers = numbers.replace(eng, str(num))
#     return int(numbers)
