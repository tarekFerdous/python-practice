# Hash maps solved unaided; sorting cost was missed in complexity analysis

Tarek solved Two Sum, Top K Words and Group Anagrams with a dict and a sorted-letters key, and all tests passed after he debugged with tracebacks and the REPL. He picked the right pattern every time. He said all three were O(n), missing the O(m log m) of `sorted()` and the per-word O(L log L) sort, and he gave no space complexity. Keep asking for time *and* space after every exercise, and use questions that hide a sort.

**Evidence**: `exercises/0001-hash-maps`, 3/3 tests green, 2026-11-02. Bugs on the way: a list returned instead of a tuple, `visited[v]` instead of `visited[target - v]` (KeyError), a lambda using the outer loop variable instead of its own parameter.

**Implications**: style habits to drill: names (`v`, `storage`), an unused `enumerate`/`i`, leftover `print`s, `split(' ')` vs `split()`. Doesn't use `Counter` or `defaultdict` yet (shown the idiomatic versions). The lambda-parameter confusion suggests a short check that `key=` gets each item.
