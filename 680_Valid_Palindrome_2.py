
#too slow

class Solution:
    def validPalindrome(self, s):

        for i in range(len(s)):

            new = [i for i in s]
            new.pop(i)
            new= ''.join(new)
            if new[0]==new[-1]:

                reverse_new = ''.join(reversed(new))
                if new == reverse_new:
                    return True





        return False



