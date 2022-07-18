class Solution:
    @staticmethod
    def solve(num1, num2):
        int_num1 = int(num1)
        int_num2 = int(num2)
        return int_num1 * int_num2


if __name__ == '__main__':
    num1 = '123'
    num2 = '456'
    print(Solution.solve(num1, num2))