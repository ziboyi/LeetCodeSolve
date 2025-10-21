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

    # 76.最小覆盖子串，滑动指针解法
    def minWindow(self, s: str, t: str) -> str:
        def str_to_dict(s):
            str_dict = {}
            for char in s:
                str_dict[char] = str_dict[char] + 1 if char in str_dict else 1
            return str_dict

        def cover(s_dict: dict, t_dict: dict) -> bool:
            for k in t_dict:
                if k not in s_dict:
                    return False
                elif s_dict[k] < t_dict[k]:
                    return False
            return True

        t_dict = str_to_dict(t)
        pos_start, pos_end = 0, 0
        min_window = ''
        window_dict = {}
        while True:
            if not cover(window_dict, t_dict):
                pos_end += 1
                if pos_end <= len(s):
                    window_dict[s[pos_end-1]] = window_dict[s[pos_end-1]] + 1 if s[pos_end-1] in window_dict else 1
            else:
                if min_window == '':
                    min_window = s[pos_start:pos_end]
                elif len(s[pos_start:pos_end]) < len(min_window):
                    min_window = s[pos_start:pos_end]
                window_dict[s[pos_start]] = window_dict[s[pos_start]] - 1
                pos_start += 1
            if pos_start == pos_end:
                pos_end += 1
                if pos_start >= len(s):
                    break
                else:
                    window_dict = {s[pos_start]: 1}
            if pos_end > len(s) + 1:
                break

        return min_window



if __name__ == '__main__':
    # words = ["This", "is", "an", "example", "of", "text", "justification."]
    # result = Solution().fullJustify(words, maxWidth=16)
    # for i in result: print(i)

    result = Solution().minWindow("ADOBECODEBANC", "ABC")
    result = Solution().minWindow("a", "a")
    result = Solution().minWindow("", "ABC")
    print(result)

