class Solution:
    @staticmethod
    def addStrings( num1: str, num2: str) -> str:
        assert 1 <= len(num1) and  len(num2) <= 104, 'Invalid input strings'
        res = ''
        carry = 0
        for cursor in range(0, min(len(num1), len(num2)), 1):
            dig1 = int(num1[-1 * (cursor + 1)])
            dig2 = int(num2[-1 * (cursor + 1)])
            sum_dig = dig1 + dig2 + carry
            carry = 0
            if sum_dig > 9:
                carry = 1
                sum_dig %= 10
            res = str(sum_dig) + res
            print(f'sum_dig= {sum_dig}, carry={carry}')
        if carry == 1:
            if max(len(num1), len(num2)) > min(len(num1), len(num2)):
                dif = max(len(num1), len(num2)) - min(len(num1), len(num2))
                if max(len(num1), len(num2)) == len(num1):
                    num_carry = int(num1[diff - 1])
                    num_carry += 1
                    res = str(num_carry) + res
                else:
                    num_carry = int(num2[diff - 1])
                    num_carry += 1
                    res = str(num_carry) + res
            else:
                 res = '1' + res
        return res
print(Solution.addStrings('899', '11'))