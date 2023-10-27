# 예상 시간 복잡도 O(n) n is s length
def solution(s, n):
    answer = [caesarEncryption(s[i],n) if str(s[i]).isalpha() else " " for i in range(0,len(s))]
    return ''.join(answer)

def caesarEncryption(char, shift):
    if str(char).islower():
        encChar = ord(char) + shift
        if encChar > ord('z'):
            encChar = ord('a') + (encChar - ord('z') - 1)
        else:
            pass
    else:
        encChar = ord(char) + shift
        if encChar > ord('Z'):
            encChar = ord('A') + (encChar - ord('Z') - 1)
        else:
            pass
    return chr(encChar)

print(solution('z',1))
