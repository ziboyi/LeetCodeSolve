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

    # 3. 无重复字符的最长子串
    def lengthOfLongestSubstring(self, s: str) -> int:
        def has_same_char(s: str): # 判断是否有重复字符
            return True if len(s) != len(set(s)) else False

        if len(s) == 0: return 0
        if len(s) == 1: return 1

        max_length = 1
        pos_start, pos_end = 0, 0
        while pos_start < len(s):
            for pos_end in range(pos_start + max_length, len(s) + 1):
                if not has_same_char(s[pos_start:pos_end]):
                    max_length = len(s[pos_start:pos_end]) if len(s[pos_start:pos_end]) > max_length else max_length
                else:
                    break
            pos_start += 1

        return max_length

    # 5. 最长回文子串
    def longestPalindrome(self, s: str) -> str:
        def reverse_string(s):
            return s[::-1]

        def is_palindrome(s): # 判断是否是回文串
            return True if reverse_string(s) == s else False

        if len(s) == 1: return s

        max_length = 1
        longest_palindrome = s[0]
        pos_start, pos_end = 0, 0
        while pos_start < len(s):
            for pos_end in range(pos_start + max_length, len(s) + 1):
                if is_palindrome(s[pos_start:pos_end]):
                    max_length = len(s[pos_start:pos_end]) if len(s[pos_start:pos_end]) > max_length else max_length
                    longest_palindrome = s[pos_start:pos_end]
            pos_start += 1
        return longest_palindrome

    # 6. Z字型变换
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1: return s

        row_list = []
        for i in range(numRows): row_list.append([])
        row_pos = 0
        row_pos_add_or_minus = 1 # 1代表加1，-1代表减1
        for char in s:
            row_list[row_pos].append(char)
            if row_pos == numRows - 1: row_pos_add_or_minus = -1
            if row_pos == 0: row_pos_add_or_minus = 1
            row_pos += row_pos_add_or_minus

        res = ''
        for i in row_list:
            for j in i:
                res += j
        return res

    # 14. 最长公共前缀
    def longestCommonPrefix(self, strs: List[str]) -> str:
        lengths = [len(i) for i in strs]
        result = ''
        for i in range(min(lengths)):
            chars = set([s[i] for s in strs])
            if len(chars) == 1:
                result += list(chars)[0]
            else:
                break
        return result

    # 17. 电话号码的字母组合
    def letterCombinations(self, digits: str) -> List[str]:
        digit_to_chars = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z'],
        }
        result = []
        for digit in digits:
            if len(result) == 0:
                result = digit_to_chars[digit]
            else:
                original_len = len(result)
                l = len(digit_to_chars[digit])
                result = result * l
                result_add = []
                for i in digit_to_chars[digit]:
                    result_add += [i] * original_len
                result = [i + j for i, j in zip(result, result_add)]
        return result

    # 22. 括号生成
    def generateParenthesis(self, n: int) -> List[str]:
        def is_valid(s: str) -> bool:
            stack = []
            try:
                for char in s:
                    if char == '(': stack.append('(')
                    else: stack.pop()
            except:
                return False
            return True

        result = ['(']
        result_count = [[1, 0]]
        for _ in range(n * 2 - 1):
            new_result = []
            new_result_count = []
            for idx, i in enumerate(result):
                count = result_count[idx]
                if is_valid(i + '(') and count[0] + 1 <= n:
                    new_result.append(i + '(')
                    new_result_count.append([count[0] + 1, count[1]])
                if is_valid(i + ')') and count[1] + 1 <= n:
                    new_result.append(i + ')')
                    new_result_count.append([count[0], count[1] + 1])
            result = new_result
            result_count = new_result_count
        return result

    # 28. 找出字符串中第一个匹配项的下标
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)

    # 30. 串联所有单词的字串
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        def words_count_dict(words: list) -> dict:
            d = {}
            for w in words:
                d[w] = 1 if w not in d else d[w] + 1
            return d

        def str_group(string, n):
            str_list = []
            for i in range(0, len(string), n):
                str_list.append(string[i:i+n])
            return str_list

        d = words_count_dict(words)
        result = []
        word_length = len(words[0])
        l = len(words) * word_length
        for pos in range(0, len(s) - l + 1):
            str_list = str_group(s[pos:pos+l], word_length)
            if words_count_dict(str_list) == d:
                result.append(pos)

        return result


if __name__ == '__main__':
    res = Solution().findSubstring("wordgoodgoodgoodbestword", ["word","good","best","word"])
    print(res)
    res = Solution().findSubstring("wordgoodgoodgoodbestword", ["w","o","r","d"])
    print(res)
