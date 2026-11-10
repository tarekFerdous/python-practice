from exercises import is_palindrome, longest_unique_substring, max_sum_of_k, pair_with_sum


def test_is_palindrome():
    assert is_palindrome("A man, a plan, a canal: Panama") is True
    assert is_palindrome("race a car") is False
    assert is_palindrome("") is True
    assert is_palindrome(" .,") is True
    assert is_palindrome("0P") is False
    assert is_palindrome("ab_a") is True


def test_pair_with_sum():
    assert pair_with_sum([1, 3, 4, 6, 9], 13) == (2, 4)
    assert pair_with_sum([1, 2, 3], 100) is None
    assert pair_with_sum([-5, -1, 0, 7], 2) == (0, 3)
    assert pair_with_sum([2, 2], 4) == (0, 1)
    assert pair_with_sum([], 1) is None
    assert pair_with_sum([1, 2, 3, 10], 5) == (1, 2)   # needs the 'too big' branch


def test_max_sum_of_k():
    assert max_sum_of_k([2, 1, 5, 1, 3, 2], 3) == 9
    assert max_sum_of_k([4], 1) == 4
    assert max_sum_of_k([-3, -1, -2], 2) == -3
    assert max_sum_of_k([1, 2, 3, 4], 4) == 10


def test_longest_unique_substring():
    assert longest_unique_substring("abcabcbb") == 3
    assert longest_unique_substring("bbbbb") == 1
    assert longest_unique_substring("pwwkew") == 3
    assert longest_unique_substring("") == 0
    assert longest_unique_substring("abba") == 2
    assert longest_unique_substring("dvdf") == 3
