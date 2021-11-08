class Solution:
    def sortSentence(self, s: str) -> str:
        sent_hash={}
        final_sent = ''

        for i in s.split():
            elemt = int(i[-1])
            word_len = len(i)-1
            word = i[:word_len]
            sent_hash[elemt]=word

        for i in range(1,len(sent_hash)+1):
            final_sent+= sent_hash[i]
            if i !=len(sent_hash):
                final_sent += ' '
        return final_sent

logs = "lGaWqAkfVIFhqBzRs3 l2 bwKhelcNiyNBpjGUN1"
s = Solution()
t = s.sortSentence(logs)
print(t)