def is_palindrome(pal):
    palindromic_string = "".join(reversed(list(pal)))
    if pal == palindromic_string:
        print(f'Word {pal} is palindrome')
    else:
        print(f'Word {pal} is not palindrome')

if __name__=='__main__':
    is_palindrome("kajak")
    is_palindrome("mars")