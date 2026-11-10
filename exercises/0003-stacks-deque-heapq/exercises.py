"""Lesson 3: stacks (list), queues (collections.deque) and heaps (heapq).

Fill in each function, then run from this folder:
    python -m pytest -q
Before coding each one, say out loud: brute force + its Big-O, then your idea.
When done, give BOTH time and space complexity for each.
"""
import heapq
from collections import deque


def is_valid_brackets(s: str) -> bool:
    """True if every ( [ { is closed by the matching ) ] } in the right order.
    s contains only bracket characters.

    is_valid_brackets("([]{})") -> True
    is_valid_brackets("([)]")   -> False
    is_valid_brackets("((")     -> False
    """
    stack = []
    bracket = {"(":")", "{":"}", "[":"]"}
    bracket_close = {")":"(", "}":"{", "]":"["}
    for i, v in enumerate(s):
        stack.append(v)
        if v in bracket_close and stack[-2] != bracket_close[v]:
            return False
        elif v in bracket_close and stack[-2] == bracket_close[v]:
            stack.pop()
            stack.pop()

    if stack:
        return False
    return True


class RecentCounter:
    """Counts requests in the last 3000 ms (a mini rate-limiter).
    ping(t) records a request at time t (ms) and returns how many requests happened
    in [t - 3000, t], including this one. Each t is larger than the one before.

    rc = RecentCounter()
    rc.ping(1)    -> 1
    rc.ping(100)  -> 2
    rc.ping(3001) -> 3
    rc.ping(3002) -> 3      # t=1 is now too old
    """

    def __init__(self):
        pass

    def ping(self, t: int) -> int:
        pass


def kth_largest(nums: list[int], k: int) -> int:
    """The k-th largest number (k=1 is the max). Duplicates count separately.
    Assume 1 <= k <= len(nums). Beat sorting: O(n log k), using a heap of size k.

    kth_largest([3, 2, 1, 5, 6, 4], 2)          -> 5
    kth_largest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4) -> 4
    """
    pass


def merge_sorted_lists(lists: list[list[int]]) -> list[int]:
    """Merge k sorted lists into one sorted list. Don't just concatenate and sort:
    use a heap holding the current smallest item of each list.

    merge_sorted_lists([[1, 4, 5], [1, 3, 4], [2, 6]]) -> [1, 1, 2, 3, 4, 4, 5, 6]
    merge_sorted_lists([[], [0]])                      -> [0]
    """
    pass


if __name__ == "__main__":
    print(is_valid_brackets("([)]"))              # expect False
