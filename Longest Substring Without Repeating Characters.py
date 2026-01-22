class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        Max = 0
        ans = []

        for i in range(len(s)):
            if s[i] in ans:
                
                Max = max(Max, len(ans))

                
                duplicate_index = ans.index(s[i])
                ans = ans[duplicate_index + 1:]

           
            ans.append(s[i])

        
        return max(Max, len(ans))

        return Max
