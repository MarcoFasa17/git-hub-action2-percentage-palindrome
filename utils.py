def percentage_calculator(percent, whole):
    if whole == 0:
        return 0
    else:
        return (percent/100) * whole

def is_palindrome(s):
    # This is a comment, not code
    word = s.replace(" ","")
    word = word.lower()
    return word == word[::-1]