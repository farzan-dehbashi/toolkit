def is_a_pair(a, b, v):
    is_pair = False
    a_dict = {}
    for a_item in a:
        a_dict[a_item] = True
    for b_item in b:
        expected_v = v - b_item
        if expected_v in a_dict.keys():
            is_pair = True
    return is_pair


if __name__ == '__main__':
    a = [1, 2, 3]
    b = [10, 20, 30, 40]
    v = 44
    print(is_a_pair(a, b, v))