input = "tomato"


def is_palindrome(string):  # is_palindrome("소주만병만주소")  "주만병만주" "만병만" "병"
    if string[0] != string[-1]:
        return False
    if len(string) <= 1:    # "병" == True
        return True

    return is_palindrome(string[1:-1])  # is_palindrome("주만병만주") "만병만" "병"

print(is_palindrome(input)) # True