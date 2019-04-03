class Solution:
    def longestPalindrome(self,s):
        if len(s) == 1:
            print(s) 
        else:
            left, right = [],[]
            si = 0
            ei = len(s)-1
            start,end = s[si],s[ei]
            
            while start == end:
                if si == ei or ei < si:
                    if len(s)%2 != 0:
                        left.append(s[si])         
                    right.reverse()
                    return "".join(left+right)
                left.append(start)
                right.append(end)
                si=si+1
                start = s[si]
                ei=ei-1
                end = s[ei]
            return self.longestPalindrome(s[1:-1])

    def romanToInt(self, s):
        dubDict = {'IV':4,'IX':9,'XL':40,'XC':90,'CD':400,'CM':900}
        singleDict = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        toAdd = 0
        for i in dubDict.items():
            subStr = i[0]
            c = s.count(subStr)
            s = s.replace(subStr,"")
            for _ in range(c):
                toAdd = toAdd + dubDict.get(subStr)
        for i in singleDict.items():
            subStr = i[0]
            c = s.count(subStr)
            s = s.replace(subStr,"")
            for _ in range(c):
                toAdd = toAdd + singleDict.get(subStr)
        return toAdd

sol = Solution()
print(sol.romanToInt('IVXCD'))