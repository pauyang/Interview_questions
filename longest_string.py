'''

Given a string s, find the length of the longest substring without repeating characters.

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

Input: s = ""
Output: 0
'''

class Solution:

    '''
    Have left and right pointer:
    initiate left ptr to position
    initiate substring by adding character of left ptr
    iterate right ptr through rest of length of strings
    if not exisit in substtring, add right ptr character to substring
    if exists: (that means it is longest length for charcter of left ptr
    1.) Remove left ptr character from substring
    2.) Increment left ptr character
    3.) Continue to remove character of left ptr until there's no right character in substring
    4.) Take the Max of previous result vs current results

    '''
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)>1:
            left =0
            substring = set()
            result = 0
            substring.add(s[left])
            for right in range(1,len(s)):
                if s[right] in substring:
                    while s[right] in substring:

                        substring.remove(s[left])
                        left+=1

                substring.add(s[right])

                result = max( result, right-left+1)

            return result
        elif len(s) ==1:
            return 1
        else:
            return 0


    '''
    # Brute Force method
        max_length =0
        if s:
            max_string = []
            count = 1
            if len(s)>1:
                for i in s:

                    substring = s[count:]
                    max_string.append(i)
                    for j in substring:
                        if j not in max_string:
                            max_string.append(j)
                        else:
                            break

                    max_length = max(max_length, len(max_string))
                    count+=1
                    max_string = []
            else:
                return 1

            max_length = max(max_length, len(max_string))
            return max_length
        else:
            return 0
    '''


s = Solution()
t = s.lengthOfLongestSubstring(" ")
print (t)