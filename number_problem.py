
from utils import find_factors
from decimal import Decimal
from typing import List



class Solution:
    # 166. 分数到小数
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        print(numerator/denominator)
        sign = '-' if numerator * denominator < 0 else ''  # 正负号
        numerator, denominator = abs(int(numerator)), abs(int(denominator))
        integer_part = numerator // denominator  # 整数部分
        if numerator % denominator == 0: ## 能整除的情况
            return ''.join([sign, str(integer_part)])
        else: ## 不能整除的情况
            numerator = numerator % denominator
            numerator_factors = find_factors(numerator)
            denominator_factors = find_factors(denominator)
            new_numerator_factors = []
            new_denominator_factors = []
            # 双指针模拟约分的过程
            pos1, pos2 = 0, 0
            while pos1 < len(numerator_factors) and pos2 < len(denominator_factors):
                if numerator_factors[pos1] == denominator_factors[pos2]:
                    pos1 += 1
                    pos2 += 1
                elif numerator_factors[pos1] > denominator_factors[pos2]:
                    new_denominator_factors.append(denominator_factors[pos2])
                    pos2 += 1
                else:
                    new_numerator_factors.append(numerator_factors[pos1])
                    pos1 += 1
            if pos1 == len(numerator_factors):
                new_denominator_factors += denominator_factors[pos2:]
            if pos2 == len(denominator_factors):
                new_numerator_factors += numerator_factors[pos1:]

            is_infinity_loop = False
            for i in new_denominator_factors:
                if i not in [2, 5]:
                    is_infinity_loop = True


            if not is_infinity_loop: # 有限小数的情况

                decimal_part = []  # 商部分
                left_part = [numerator]  # 余数部分
                # 模拟长除法的过程
                while True:
                    # 商为a，余数为b
                    a = numerator * 10 // denominator
                    b = numerator * 10 % denominator
                    decimal_part.append(a)
                    if b == 0:  # 余数部分开始循环
                        break
                    else:
                        numerator = b
                        left_part.append(b)

                return ''.join([
                    sign,
                    str(integer_part),
                    '.',
                    ''.join([str(i) for i in decimal_part])
                ])
            else: # 无限不循环小数的情况
                decimal_part = [] # 商部分
                left_part = [numerator] # 余数部分
                # 模拟长除法的过程
                while True:
                    # 商为a，余数为b
                    a = numerator * 10 // denominator
                    b = numerator * 10 % denominator
                    decimal_part.append(a)
                    if b in left_part: # 余数部分开始循环
                        loop_position_start = left_part.index(b)
                        break
                    else:
                        numerator = b
                        left_part.append(b)

                return ''.join([
                    sign,
                    str(integer_part),
                    '.',
                    ''.join([str(i) for i in decimal_part[:loop_position_start]]),
                    '(',
                    ''.join([str(i) for i in decimal_part[loop_position_start:]]),
                    ')'
                ])

    # 60. 排列序列
    def getPermutation(self, n: int, k: int) -> str:
        numbers_list = [str(i) for i in range(1, n+1)]
        k = k - 1 # k从1开始排序，改成从0开始排序。
        def factorial(n: int):
            res = 1
            for i in range(1, n + 1):
                res *= i
            return res

        l = [] # 第i位是排第几的数字
        while n > 1:
            number = k // factorial(n-1)
            l.append(number)
            k = k % factorial(n - 1)
            n -= 1

        result = ''
        for i in l:
            result = result + numbers_list.pop(i)
        result = result + numbers_list.pop()
        return result

    # 7. 整数反转
    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1
        x = sign * x
        result = 0
        while x >= 10:
            result = result * 10 + x % 10
            x = x // 10
        result = result * 10 + x % 10
        result = sign * result
        if result > 2 ** 31 - 1 or result < - 2 ** 31:
            return 0
        else:
            return result

    # 8. 字符串转换整数
    def myAtoi(self, s: str) -> int:
        if s.strip() == '': return 0
        s = s.strip()

        if s[0] not in {'-', '+', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}:
            return 0

        if s[0] == '-':
            sign = -1
            new_s = s[1:]
        elif s[0] == '+':
            sign = 1
            new_s = s[1:]
        else:
            sign = 1
            new_s = s
        number = 0
        d = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
        for char in new_s:
            if char not in d:
                break
            new_number = number * 10 + d[char]
            if sign * new_number > 2 ** 31 - 1:
                return 2 ** 31 - 1
            elif sign * new_number < - 2 ** 31:
                return - 2 ** 31
            else:
                number = new_number

        return sign * number


    # 9. 回文数
    def isPalindrome(self, x: int) -> bool:
        def reverse_string(s):
            return s[::-1]

        if x < 0: return False
        x_reverse = reverse_string(str(x))
        if int(x_reverse) == x: return True
        else: return False








if __name__ == "__main__":
    # result = Solution().fractionToDecimal(1, 2147483648)
    # result = Solution().getPermutation(3, 1)
    # print(result)

    # result = Solution().reverse(42)
    # print(result)

    # result = Solution().myAtoi("   -042")
    # print(result)

    res = Solution().isPalindrome(121)
    print(res)



