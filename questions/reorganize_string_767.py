class Solution:
    @staticmethod
    def count_chars(s):
        chars = {}
        for char in s:
            if char in chars.keys():
                chars[char] += 1
            else:
                chars[char] = 1
        return chars

    @staticmethod
    def find_max_val(vals_list):
        max_val = 0
        for key in vals_list:
            if vals_list[key] > max_val
                max_val = vals_list[key]
        for key in vals_list:
            if vals_list[key] == max_val:
                return key

    @staticmethod
    def reorganize_string(s):
        assert len(s) > 0 and len(s) <= 500 and s==s.lower() and s.isalpha() == True, 'Invalid string - reorganize_string()'
        char_dict = Solution.count_chars(s)
        res = ''
        vals_list = list(char_dict.values())
        while vals_list:
            mex_key = Solution.find_max_val(vals_list)
            


        
        return res


if __name__ == '__main__':
    print(Solution.reorganize_string(s = 'aabbcaa'))