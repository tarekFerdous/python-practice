# Python Coding Interview Resources

## Knowledge

- [Tech Interview Handbook: Hash table](https://www.techinterviewhandbook.org/algorithms/hash-table/)
  Concise interview-focused overview: space-time tradeoff, O(1) average ops, essential questions (Two Sum, Ransom Note) and recommended ones (Group Anagrams, LRU Cache). Use for: the primary reading of each topic; the site has one page per data structure.
- [Python docs: Time complexity of built-in types](https://docs.python.org/3/builtins/time-complexity.html)
  Official Big-O table for list, dict, set, deque. Use for: citing any complexity claim (e.g. `x in list` is O(n), `x in set` is O(1) average).
- [Python docs: collections](https://docs.python.org/3/library/collections.html)
  Official reference for Counter, defaultdict, deque. Use for: exact behaviour (e.g. `most_common` ties come in first-encountered order; `defaultdict.get()` does not call the factory).
- [Python docs: Sorting HOW TO](https://docs.python.org/3/howto/sorting.html)
  Key functions, stability, multi-key sorts with tuples. Use for: any custom sort order question.
- [Python docs: The Python Tutorial](https://docs.python.org/3/tutorial/)
  Official language tour. Use for: syntax refreshers (comprehensions, classes, exceptions) when basics are rusty.

- [Tech Interview Handbook: Array](https://www.techinterviewhandbook.org/algorithms/array/)
  Sliding window and two pointers sections: same-direction pointers that never overtake keep it O(n). Lists Best Time to Buy and Sell Stock, Container With Most Water. Use for: Lesson 2 primary reading.
- [Tech Interview Handbook: String](https://www.techinterviewhandbook.org/algorithms/string/)
  Pointers from both ends for palindromes; essential questions Valid Palindrome and Longest Substring Without Repeating Characters. Use for: string problem lists.
- [Python docs: str methods](https://docs.python.org/3/library/stdtypes.html#string-methods)
  isalnum, lower, strip, split. Use for: exact string behaviour.

## Wisdom (Communities)

- [LeetCode Discuss](https://leetcode.com/discuss/)
  Solutions and interview experiences per problem. Use for: comparing your solution to others after solving (never before).
- [r/learnpython](https://www.reddit.com/r/learnpython/)
  Large, well-moderated beginner-friendly subreddit. Use for: "why does this Python behave like this?" questions.

## Gaps
- No verified source yet for AI-flavoured interview tasks (chunking, cosine top-k, LLM JSON validation). Find one before lesson 6.
- The target company's actual test format is unknown.
