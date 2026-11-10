"""Tiny test runner for the exercise notebooks.

    check(two_sum, [
        (([2, 7, 11, 15], 9), (0, 1)),   # (args tuple, expected)
    ])

Prints one line per case: what you called, what you got, what was expected.
Exceptions are caught and shown instead of stopping the notebook.
"""
import copy

GREEN, RED, RESET = "\033[32m", "\033[31m", "\033[0m"


def check(fn, cases, name=None):
    name = name or getattr(fn, "__qualname__", repr(fn))
    passed = 0
    for args, expected in cases:
        if not isinstance(args, tuple):
            args = (args,)
        shown = ", ".join(repr(a) for a in args)
        try:
            got = fn(*copy.deepcopy(args))
        except Exception as e:  # show the crash, keep going
            got = f"<{type(e).__name__}: {e}>"
        ok = got == expected and type(got) is type(expected)
        passed += ok
        mark = f"{GREEN}PASS{RESET}" if ok else f"{RED}FAIL{RESET}"
        line = f"{mark}  {name}({shown}) -> {got!r}"
        if not ok:
            line += f"   expected {expected!r}"
        print(line)
    colour = GREEN if passed == len(cases) else RED
    print(f"{colour}{passed}/{len(cases)} passed{RESET}\n")
    return passed == len(cases)
