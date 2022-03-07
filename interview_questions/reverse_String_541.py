def reverse(string):
    string = list(string)
    string.reverse()
    string = ''.join(string)
    return string


def reverse_complex_string(string, k):
    assert len(string) <= 10000 and len(string) >= 1 and k  <= 10000 and k >= 1, 'K or string values are not as expected!'

    cursor = 0
    res = ''
    while cursor < len(string) :
        print(f'cursor= {cursor}')
        if (cursor + 1) % k == 0 and cursor > 0:
            start_p = cursor - k + 1
            end_p = cursor + 1
            reverse_bit = string[start_p: end_p]
            reverse_bit = reverse(reverse_bit)
            res += reverse_bit
            print(f'--- cursor= {cursor}, res= {res}, revese_bit = {reverse_bit}, res= {res}')
        if cursor >= len(string) - (len(string) % k):
            res += string[cursor]
            
        cursor += 1
    return res
if __name__ == '__main__':
    print(reverse_complex_string('abcdefg', k = 2))
