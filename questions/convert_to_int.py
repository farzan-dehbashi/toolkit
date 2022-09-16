def myAtoi(s):
    s = s.replace(' ','')
    is_negative = False
    s = list(s)

    if s[0] == '-':
        del s[0]
        is_negative = True
    if s[0] == '+':
        del s[0]
    s_temp = []
    found_char = False
    for index, char in enumerate(s):
        if char.isdigit() == False:
            found_char = True
        if char.isdigit() and found_char == False:
           s_temp.append(char)

    s = s_temp
    if len(s) == 0:
        s.append(list('0000'))
    while s[0] == '0':
        del s[0]
    if len(s) > 10:
        if is_negative == False:
            s = list(str(2147483648-1))
        else:
            s = list(str(-2147483648))
    result_string = ''
    for char in s:
        result_string = result_string + char
    if is_negative == True:
        result = -1 * int(result_string)
    else:
        result = int(result_string)
    return result

print(myAtoi('sdf 4193 with words'))