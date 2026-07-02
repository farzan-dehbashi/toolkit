def is_palindrome(s):
    s = s.lower().replace(" ", "")
    return s == s[::-1]


def is_palindrome_two_pointer(s):
    s = s.lower().replace(" ", "")
    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True


if __name__ == "__main__":
    print(is_palindrome("racecar"))        # True
    print(is_palindrome("A man a plan a canal Panama"))  # True
    print(is_palindrome("hello"))          # False
    print(is_palindrome_two_pointer("racecar"))  # True
