from exercises import RecentCounter, is_valid_brackets, kth_largest, merge_sorted_lists


def test_is_valid_brackets():
    assert is_valid_brackets("([]{})") is True
    assert is_valid_brackets("([)]") is False
    assert is_valid_brackets("((") is False
    assert is_valid_brackets("))") is False
    assert is_valid_brackets("") is True
    assert is_valid_brackets("{[()()]}") is True
    assert is_valid_brackets("]") is False


def test_recent_counter():
    rc = RecentCounter()
    assert rc.ping(1) == 1
    assert rc.ping(100) == 2
    assert rc.ping(3001) == 3
    assert rc.ping(3002) == 3
    assert rc.ping(10000) == 1


def test_kth_largest():
    assert kth_largest([3, 2, 1, 5, 6, 4], 2) == 5
    assert kth_largest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4) == 4
    assert kth_largest([7], 1) == 7
    assert kth_largest([-1, -5, -3], 3) == -5


def test_merge_sorted_lists():
    assert merge_sorted_lists([[1, 4, 5], [1, 3, 4], [2, 6]]) == [1, 1, 2, 3, 4, 4, 5, 6]
    assert merge_sorted_lists([[], [0]]) == [0]
    assert merge_sorted_lists([]) == []
    assert merge_sorted_lists([[5, 5], [5]]) == [5, 5, 5]
