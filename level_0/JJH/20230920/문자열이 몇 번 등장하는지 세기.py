def solution(myString, pat):
    answer = 0
    String = myString
    while pat in String:
        answer = answer + 1
        String = String[String.find(pat)+1 :]
    return answer
