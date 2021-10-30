'''

Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.

A substring is a contiguous sequence of characters within the string.

Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.

Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.

Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.


'''


class Solution:
    def minWindow(self, s, t):
        left =0
        found = ''

        window =dict.fromkeys(list(t),0)
        countT = dict.fromkeys(list(t),0)
        for i in t:
            countT[i]=t.count(i)


        have, need = 0, len(t)

        for right in range(len(s)):
            temp_window =s[left:right+1]
            if s[right] in t and (have < need):
                window[s[right]]=window[s[right]]+1
                if window[s[right]] <= countT[s[right]]:
                    have +=1

            while have == need:



                #found.append(temp_window)
                #recalculate window matching

                for i in temp_window:
                    temp_window = s[left:right + 1]
                    left += 1
                    if i in window.keys():
                        window[i]=window[i]-1

                        if len(temp_window)<len(found) or found =='':
                            found=temp_window

                        if window[i]<countT[i]:
                            #found.append(temp_window)
                            have-=1
                            break


        return found

















s = "ADOBECODEBANC"
t = "ABC"

test=Solution()
print(test.minWindow(s,t))






















