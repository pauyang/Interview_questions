

class Solution:
    def wordSquares(self, words):
        result=[]
        for word in words:
            temp = self.backtrack([word],words)
            if temp:
                result.append(self.backtrack([word],words))

        return result


    def backtrack(self,current,words):
        result=[]
        if len(current)==len(current[0]):
            return list(current)

        else:

            prefix = self.get_current_prefix(current)
            for candidate in self.check_match_prefix_word(prefix,words):
                current.append(candidate)
                result.append(self.backtrack(current,words))
                if len(current)==len(current[0]):
                    return list(current)
                else:
                    current.pop()


    def get_current_prefix (self,current):

        prefix =''.join(word[len(current)] for word in current)

        return prefix

    def check_match_prefix_word(self,prefix,words):

        match =[word for word in words if word.startswith(prefix)]

        return match












words = ["area","lead","wall","lady","ball"]
s = Solution()
t = s.wordSquares(words)
print(t)















