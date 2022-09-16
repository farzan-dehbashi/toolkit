class Solution:
    @staticmethod
    def reverseWords(s) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        string = ''.join(s)
        string = string.split()
        string = ' '.join(string)
        return list(string)
        

print(Solution.reverseWords(s = ["t","h","e"," ","s","k","y"," ","i","s"," ","b","l","u","e"]))