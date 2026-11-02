"""Highlight non-overlapping matches. Run: python -m java6.detyra3.main"""

from java6.detyra2.main import findAll


def highlight(T, P):
    """Find every occurrence and copy the text character by character."""
    positions = findAll(T, P)
    # Empty matches have no characters to enclose, so preserve the text.
    if not P or not positions:
        return T

    result = []
    cursor = 0
    for start in positions:
        # cursor is just past the previous highlighted occurrence.
        if start < cursor:
            continue
        while cursor < start:
            result.append(T[cursor])
            cursor += 1
        result.append("[")
        end = start + len(P)
        while cursor < end:
            result.append(T[cursor])
            cursor += 1
        result.append("]")

    # Preserve all characters after the final highlighted occurrence.
    while cursor < len(T):
        result.append(T[cursor])
        cursor += 1
    # Join once instead of repeatedly copying an ever-growing string.
    return "".join(result)


if __name__ == "__main__":
    print(highlight("Kur ngjite përpjetë, shiko dhe tatëpjetë.", "pjetë"))
    print(highlight("banana", "ana"))
