from utils import percentage_calculator, is_palindrome

def test_percentage_calculator():
    assert percentage_calculator(20, 10) == 2
    assert percentage_calculator(0, 100) == 0
    assert percentage_calculator(5, 0) == 0

def test_is_palindrome():
    assert is_palindrome("madam")
    assert is_palindrome("racecar")
    assert not is_palindrome("Good Morning")