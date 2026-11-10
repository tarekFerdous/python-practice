"""Lesson 1: hash maps (dict, Counter, defaultdict) + sorting with a key.

Fill in each function, then run from this folder:
    python -m pytest -q
Aim for 10-15 minutes per exercise. Say the time and space complexity out loud when done.
"""


def two_sum(nums: list[int], target: int) -> tuple[int, int]:
    """Return the indices (i, j), i < j, of the two numbers that add up to target.
    Exactly one answer exists. Must be O(n), not the O(n^2) double loop.

    two_sum([2, 7, 11, 15], 9) -> (0, 1)
    two_sum([3, 2, 4], 6)      -> (1, 2)
    """
    visited = {}
    for i, v in enumerate(nums):
        remain = target - v
        if remain in visited:
            return (visited[remain], i)
        visited[v] = i


def top_k_words(text: str, k: int) -> list[str]:
    """Return the k most frequent words, lowercase.
    Ties: alphabetical order. Words are separated by whitespace; strip . , ! ? from them.

    top_k_words("the cat and the hat. The end!", 2) -> ["the", "and"]
    """
    text = text.replace('.', '').replace(',', '').replace('!', '').replace('?', '').lower()
    text = text.split(' ')
    print(text)
    words = {}
    for i, word in enumerate(text):
        if word in words:
            words[word] +=1
        else:
            words[word] = 1
    
    return list(sorted(words, key=lambda w: (-words[w], w)))[0:k]


def group_anagrams(words: list[str]) -> list[list[str]]:
    """Group words that are anagrams of each other.
    Keep each group in input order; order the groups by first appearance.

    group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
      -> [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]
    """
    storage = {}
    for i, v in enumerate(words):
        word = ''.join(sorted(list(v)))
        if word in storage:
            storage[word].append(v)
        else:
            storage[word] = [v]
    return [storage[v] for v in storage]


# ---------------------------------------------------------------------------
# Teacher's versions (idiomatic). Compare with yours above; rewrite from memory.
# ---------------------------------------------------------------------------
from collections import Counter, defaultdict
import heapq


def two_sum_v2(nums: list[int], target: int) -> tuple[int, int]:
    # O(n) time, O(n) space
    seen = {}                                   # value -> index
    for i, num in enumerate(nums):
        if target - num in seen:
            return (seen[target - num], i)      # earlier index is always smaller
        seen[num] = i


def top_k_words_v2(text: str, k: int) -> list[str]:
    # O(n + m log m) time, O(m) space  (n words, m distinct)
    words = [w.strip(".,!?").lower() for w in text.split()]
    counts = Counter(words)
    return sorted(counts, key=lambda w: (-counts[w], w))[:k]


def top_k_words_heap(text: str, k: int) -> list[str]:
    # O(n + m log k) time: better when k is much smaller than m
    counts = Counter(w.strip(".,!?").lower() for w in text.split())
    return heapq.nsmallest(k, counts, key=lambda w: (-counts[w], w))


def group_anagrams_v2(words: list[str]) -> list[list[str]]:
    # O(n * L log L) time, O(n * L) space  (L = word length)
    groups = defaultdict(list)
    for w in words:
        groups["".join(sorted(w))].append(w)
    return list(groups.values())


def group_anagrams_count_key(words: list[str]) -> list[list[str]]:
    # O(n * L) time: letter counts as the key instead of sorting each word
    groups = defaultdict(list)
    for w in words:
        key = [0] * 26
        for ch in w:
            key[ord(ch) - ord("a")] += 1
        groups[tuple(key)].append(w)            # lists can't be dict keys; tuples can
    return list(groups.values())


if __name__ == "__main__":
    print(two_sum_v2([3, 2, 4], 6))                                  # (1, 2)
    print(top_k_words_v2("the cat and the hat. The end!", 2))        # ['the', 'and']
    print(top_k_words_heap("b a c b a", 3))                          # ['a', 'b', 'c']
    print(group_anagrams_v2(["eat", "tea", "tan", "ate", "nat", "bat"]))
    print(group_anagrams_count_key(["eat", "tea", "tan", "ate", "nat", "bat"]))
    print(two_sum([2, 7, 11, 15], 9))   # expect (0, 1)
    print(two_sum([3, 2, 4], 6))        # expect (1, 2)
    top_k_words("the cat and the hat. The end!", 2)
    group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
