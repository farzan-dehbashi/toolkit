def isValid(s: str) -> bool:
    if len(s) <= 1:
        return False
    stack = []
    is_valid = True
    for char in s:
        # print(f' char ={char}, stack={stack}')
        if char == '(' or char == '[' or char == '{':
            stack.append(char)
        elif char == ')' or char == ']' or char == '}':
            if len(stack) == 0:
                return False
            head = stack.pop()
            if (head == '(' and char != ')') or (head == '{' and char != '}') or (head == '[' and char != ']'):
                is_valid = False
    if len(stack) != 0:
        is_valid = False
    return is_valid


print(isValid('){'))