# 예상 시간복잡도: O(N)
import re
def solution(new_id):
    new_id = new_id.lower()     
    new_id = ''.join([i if 'a'<=i<='z' or '0'<=i<='9' or i in ['-','_','.'] else '' for i in new_id])
    new_id = re.sub(r'\.+', '.', new_id)
    new_id = new_id.strip('.')
    new_id = 'a' if not new_id else new_id
    new_id = new_id[:15].strip('.')
    new_id += new_id[-1] * max(0, 3-len(new_id)) # ljust
    
    return new_id
