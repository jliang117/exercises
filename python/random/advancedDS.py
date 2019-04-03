from collections import Counter
def countChars(word):
    c = Counter()
    for w in word:
        c[w] += 1
    return c

# c = countChars('testtttesttesttest')

from collections import deque

def dequePlay():
    d = deque()
    d.appendleft('WOO')
    d.appendleft('123')
    d.append('OOW')
    d.append('321')
    
    dStr = "".join(d)
    print(dStr)
    bStr = dStr[::-1]
    print(bStr)
    isPalindrome = dStr == bStr
    print(isPalindrome)

dequePlay()


