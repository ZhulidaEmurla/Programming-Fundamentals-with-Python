def palindrome_checker(list):
    result = ''
    for num in list:
        is_palindrome = num[0] == num[-1]
        result += str(is_palindrome) + '\n'
    return result.rstrip()


positive_ints = input().split(", ")
print(palindrome_checker(positive_ints))