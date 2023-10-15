def palindrome_filtered(word):
    if word == word[::-1]:
        return word

words = input().split()
palidrome_word = input()

palidrome_list = [word for word in words if palindrome_filtered(word)]
palidrome_counter = palidrome_list.count(palidrome_word)

print(palidrome_list)
print(f'Found palindrome {palidrome_counter} times')
