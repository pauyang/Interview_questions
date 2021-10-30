class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        left = 0
        substring = ''
        max = 0
        maxstring = []
        substring += s[left]
        for right, char in enumerate(s[1:]):
            if char in substring:
                if max <1:
                    max +=1
                    substring+=char
                    maxstring.append(substring)
                else:
                    maxstring.append(substring)
                    substring = ''
            else:
                substring += char
        maxstring.append(substring)

        return (len(max(maxstring)))

s="ccaabb"
p=Solution()
result = p.lengthOfLongestSubstringTwoDistinct(s)
print (result)