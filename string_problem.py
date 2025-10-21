from typing import List

class Solution:
    # 68.文本左右对齐
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        line = []
        line_list = []
        for w in words:
            if len(' '.join(line + [w])) > maxWidth:
                line_list.append(line)
                line = [w]
            else:
                line.append(w)
        line_list.append(line)

        blank_list = []
        for line in line_list:
            if len(line) == 1:
                blanks = [' ' * (maxWidth - len(line[0]))]
                blank_list.append(blanks)
            else:
                blanks_count = len(line) -1
                total_blanks_len = maxWidth - len(''.join(line))
                blanks = [' ' * (total_blanks_len // blanks_count)] * blanks_count
                for i in range(total_blanks_len % blanks_count):
                    blanks[i] = ' ' * ((total_blanks_len // blanks_count) + 1)
                blank_list.append(blanks + [''])

        new_line_list = []
        for i, j in zip(line_list, blank_list):
            line = ''
            for word, blank in zip(i, j):
                line = line + word + blank
            new_line_list.append(line)

        last_line = new_line_list[-1]
        last_line = ' '.join(last_line.split())
        last_line = last_line + ' ' * (maxWidth - len(last_line))
        new_line_list[-1] = last_line
        return new_line_list

    # 76.最小覆盖子串
    def minWindow(self, s: str, t: str) -> str:
        pass


if __name__ == '__main__':
    words = ["This", "is", "an", "example", "of", "text", "justification."]
    result = Solution().fullJustify(words, maxWidth=16)
    for i in result: print(i)

