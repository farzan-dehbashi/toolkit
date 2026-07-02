class Solution:
    @staticmethod
    def divide(dividend: int, divisor: int) -> int:
        INT_MAX = 2**31 - 1
        INT_MIN = -(2**31)

        if dividend == INT_MIN and divisor == -1:
            return INT_MAX

        negative = (dividend < 0) != (divisor < 0)
        dividend, divisor = abs(dividend), abs(divisor)

        quotient = 0
        while dividend >= divisor:
            temp, multiple = divisor, 1
            while dividend >= (temp << 1):
                temp <<= 1
                multiple <<= 1
            dividend -= temp
            quotient += multiple

        return -quotient if negative else quotient


if __name__ == "__main__":
    print(Solution.divide(10, 3))    # 3
    print(Solution.divide(-1, -1))   # 1
    print(Solution.divide(7, -2))    # -3
