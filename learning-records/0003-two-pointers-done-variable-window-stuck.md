# Two pointers and fixed window solved; variable window needed the answer

Tarek solved Valid Palindrome, pair sum in a sorted list and max sum of k with tests passing. He got stuck on Longest Substring Without Repeating Characters and asked for the solution (a last-seen dict that jumps `left` past the earlier copy). His attempt only compared `s[left]` with `s[right]`, so it missed repeats in the middle of the window.

**Evidence**: `exercises/0002-two-pointers-sliding-window`, 2026-11-04/05. Hidden bugs: `pair_with_sum` had `right += 1` in the "too big" branch (the tests never reached it; a new test now does). `is_palindrome` built a cleaned copy, so it was O(n) space, not the O(1) the task asked for.

**Implications**: the variable window (grow right, shrink left while invalid) is not yet automatic. Revisit it in a later warm-up or the mock (e.g. longest subarray with sum ≤ k). He stops once tests pass, so ask him to check every branch runs. Teacher `_v2` versions added for is_palindrome and max_sum_of_k.
