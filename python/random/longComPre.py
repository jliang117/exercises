import trie
class Solution:
    def longestCommonPrefix(self, strs):
        t = trie.makeTrie(strs)
        print(trie.getLongestPath(t))
    

sol = Solution()
sol.longestCommonPrefix(['dogi','doggo','doge','dog'])
sol.longestCommonPrefix(['flower','flow','flowable','flowzer'])