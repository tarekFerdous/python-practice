from exercises import group_anagrams, top_k_words, two_sum


def test_two_sum():
    assert two_sum([2, 7, 11, 15], 9) == (0, 1)
    assert two_sum([3, 2, 4], 6) == (1, 2)
    assert two_sum([3, 3], 6) == (0, 1)
    assert two_sum([-1, 5, 10, -4], 6) == (2, 3)


def test_top_k_words():
    assert top_k_words("the cat and the hat. The end!", 2) == ["the", "and"]
    assert top_k_words("b a c b a", 3) == ["a", "b", "c"]
    assert top_k_words("Hi! hi? HI.", 1) == ["hi"]


def test_group_anagrams():
    assert group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]) == [
        ["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]
    assert group_anagrams([]) == []
    assert group_anagrams(["a"]) == [["a"]]
