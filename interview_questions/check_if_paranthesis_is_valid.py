


def is_valid_par(string):
    stack = []
    is_valid = True
    for char in string:
        if char == '(':
            stack.append(True)
        if char == ')':
            if len(stack) == 0:
                is_valid = False
            else:
                stack.pop()
    return is_valid


if __name__ == '__main__':
    string = '()((()))(()))'
    print(is_valid_par(string))