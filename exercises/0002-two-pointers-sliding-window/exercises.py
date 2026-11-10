"""Lesson 2: two pointers and the sliding window.

Fill in each function, then run from this folder:
    python -m pytest -q
Before coding each one, say out loud: brute force + its Big-O, then your idea.
When done, give BOTH time and space complexity for each.
"""


def is_palindrome(s: str) -> bool:
    """True if s reads the same both ways, ignoring case and anything that isn't a letter or digit.
    Use two pointers from both ends. O(1) extra space: don't build a cleaned copy.

    is_palindrome("A man, a plan, a canal: Panama") -> True
    is_palindrome("race a car")                     -> False
    """
    s = s.lower()
    s = "".join(c for c in s if c.isalnum())
    # print(s)
    left, right = 0, len(s)-1
    counter = 0
    while left<right:
        if s[left] != s[right]:
            return False
        else:
            left +=1
            right -=1
    return True


def pair_with_sum(nums: list[int], target: int) -> tuple[int, int] | None:
    """nums is sorted ascending. Return the indices (i, j), i < j, of two numbers that add up to
    target, or None if there are none. At most one pair adds up to target.
    O(n) time and O(1) space: no dict this time.

    pair_with_sum([1, 3, 4, 6, 9], 13) -> (2, 4)    # 4 + 9
    pair_with_sum([1, 2, 3], 100)      -> None
    """
    left, right = 0, len(nums)-1
    while left < right:
        if nums[left] + nums[right] == target:
            return (left, right)
        elif nums[left] + nums[right] < target:
            left +=1
        else:
            right +=1
        
    return None


def max_sum_of_k(nums: list[int], k: int) -> int:
    """Largest sum of any k consecutive numbers. Assume 1 <= k <= len(nums).
    Fixed-size window: O(n), not O(n * k).

    max_sum_of_k([2, 1, 5, 1, 3, 2], 3) -> 9        # 5 + 1 + 3
    """
    k_reached = 0
    sum = 0
    maxSum = 0
    
    for i, v in enumerate(nums):
        if k_reached<k:
            sum = sum + v
            maxSum = sum
        else:
            sum = sum + v - nums[i-k]
        

        k_reached += 1
        
        if sum > maxSum and k_reached >= k:
            maxSum = sum
    return maxSum


def longest_unique_substring(s: str) -> int:
    """Length of the longest substring with no repeated characters.
    Variable-size window: grow on the right, shrink from the left when a repeat appears.

    longest_unique_substring("abcabcbb") -> 3       # "abc"
    longest_unique_substring("pwwkew")   -> 3       # "wke"
    """
    last_seen = {}  # char -> index where it was last seen
    left = 0        # start of the current window (no repeats inside it)
    best = 0
    for right, c in enumerate(s):
        # If c already appears inside the window, move left just past that copy.
        if c in last_seen and last_seen[c] >= left:
            left = last_seen[c] + 1
        last_seen[c] = right
        best = max(best, right - left + 1)
    return best


# ---- Teacher's idiomatic versions (read after yours pass) ----

def is_palindrome_v2(s: str) -> bool:
    # O(n) time, O(1) space: skip junk by moving one pointer, no cleaned copy
    left, right = 0, len(s) - 1
    while left < right:
        if not s[left].isalnum():
            left += 1
        elif not s[right].isalnum():
            right -= 1
        elif s[left].lower() != s[right].lower():
            return False
        else:
            left += 1
            right -= 1
    return True


def max_sum_of_k_v2(nums: list[int], k: int) -> int:
    # O(n) time, O(1) space
    window = sum(nums[:k])
    best = window
    for right in range(k, len(nums)):
        window += nums[right] - nums[right - k]   # in one, out one
        best = max(best, window)
    return best


if __name__ == "__main__":
    print(is_palindrome("race a car"))              # expect False
