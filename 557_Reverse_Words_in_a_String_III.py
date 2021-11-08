class Solution:
    def reverseWords(self, s: str) -> str:
        new_list = []
        s_list = s.split()
        for i in s_list:
            word = [char for char in i]
            word.reverse()
            new_list.append(''.join(word))

        return ' '.join(new_list)

logs = "Let's take LeetCode contest"
s = Solution()
t = s.reverseWords(logs)
print(t)