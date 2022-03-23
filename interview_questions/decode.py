class Solution:
    @staticmethod
    def decodeString(s) -> str:
        res = ''
        for index, char in enumerate(s):
            if char.isdigit():
                counter = 0
                rep = int(char)
                b_index = index + 2
                while b_index < len(s) and counter >= 0:
                    print(f'b_index={b_index} char= {s[b_index]}')
                    brac = s[b_index]
                    if brac == '[':
                        counter += 1
                    if brac == ']':
                        counter -= 1
                    b_index += 1
                b_index -= 1
                print(s[index+2:b_index])
                # print(f'decoded= {Solution.decodeString(s[index+2:b_index])}')
                for i in range(0, rep):
                    res = res + Solution.decodeString(s[index+2:b_index])
                index = b_index + 1
            elif char != '[' and char != ']':
                res = res + char
        return res                

print(Solution.decodeString('3[a2[c]]ef'))