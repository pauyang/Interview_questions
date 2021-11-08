class Solution:
    def reorderSpaces(self, text: str) -> str:
        spaceN = text.count(' ')
        wordN = len(text.split())
        new_string = ''
        space = ''
        end_space = ''

        if spaceN - (wordN - 1) == 0:
            return text

        elif wordN - 1 == 0:
            for i in range(spaceN):
                space += ' '
            new_string = text.split()[0] + space



        else:

            if spaceN % (wordN - 1) == 0:
                for i in range(spaceN // (wordN - 1)):
                    space += ' '

                for i, char in enumerate(text.split()):

                    if i == len(text.split()) - 1:
                        new_string += char
                    else:

                        word_space = char + space
                        new_string += word_space


            else:
                for i in range(spaceN // (wordN - 1)):
                    space += ' '

                for i in range(spaceN % (wordN - 1)):
                    end_space += ' '

                for i, char in enumerate(text.split()):

                    if i == len(text.split()) - 1:
                        new_string += char
                    else:

                        word_space = char + space
                        new_string += word_space

                new_string += end_space

        return new_string

logs = " wywd"
s = Solution()
t = s.reorderSpaces(logs)
print(t)