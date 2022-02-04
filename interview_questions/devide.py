class Solution:
    @staticmethod
    def devide(dividend, divisor):
        if dividend < 0:
            divid_s = False
            dividend *= -1
        else:
            divid_s = True
        if divisor < 0:
            divis_s = False
            divisor *= -1
        else:
            divis_s = True
        print(f'unsigned divid = {dividend}, unsighed divis = {divisor}, {divid_s}, {divis_s} ')
        quotient = 0
        while dividend >= divisor:
            if divisor == 1:
                quotient = dividend
                break
            quotient += 1
            dividend -= divisor
        if (divis_s == True and divid_s == True) or (divis_s == True and divid_s == True):
            return quotient
        else:
            quotient *= -1
            return quotient

if __name__ == '__main__':
    print(Solution.devide(-1, -1))