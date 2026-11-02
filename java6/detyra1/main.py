"""Shared counters and Task 1 algorithms. Run: python -m java6.detyra1.main"""

_comparisons = 0
_alignments = 0


def resetCounters():
    """Start a new measurement; searches otherwise accumulate their counts."""
    global _comparisons, _alignments
    _comparisons = 0
    _alignments = 0


def getCounters():
    # A fresh dictionary prevents callers from modifying the stored counters.
    return {"comparisons": _comparisons, "alignments": _alignments}


def record_alignment():
    """Count one placement of a nonempty pattern against the text."""
    global _alignments
    _alignments += 1


def compare_characters(pattern_character, text_character):
    """Count every comparison, including the one that fails."""
    global _comparisons
    _comparisons += 1
    return pattern_character == text_character


def shiftTable(P):
    """Store distances from each character to the last pattern position."""
    m = len(P)
    table = {}
    # Excluding the final character keeps every shift positive. Repeated
    # characters overwrite earlier entries with the rightmost distance.
    for j in range(m - 1):
        table[P[j]] = m - 1 - j
    return table


def bruteForce(T, P):
    """Compare left to right at every possible starting position."""
    n, m = len(T), len(P)
    if m == 0:
        return 0

    for start in range(n - m + 1):
        record_alignment()
        j = 0
        while j < m and compare_characters(P[j], T[start + j]):
            j += 1
        if j == m:
            return start
    return -1


def horspool(T, P):
    """Compare right to left; shift on the character at the window end."""
    n, m = len(T), len(P)
    if m == 0:
        return 0

    table = shiftTable(P)
    i = m - 1
    while i < n:
        record_alignment()
        k = 0
        while k < m and compare_characters(P[m - 1 - k], T[i - k]):
            k += 1
        if k == m:
            return i - m + 1
        # Characters absent from the table permit a full-pattern shift.
        i += table.get(T[i], m)
    return -1


def horspool2(T, P):
    """Retain the lecture variant for study; its shifts can miss matches."""
    n, m = len(T), len(P)
    if m == 0:
        return 0

    table = shiftTable(P)
    i = m - 1
    while i < n:
        record_alignment()
        k = 0
        while k < m and compare_characters(P[m - 1 - k], T[i - k]):
            k += 1
        if k == m:
            return i - m + 1
        # This intentionally uses the mismatch character. The unadjusted
        # shift may jump over a match, unlike Horspool's window-end rule.
        i += table.get(T[i - k], m)
    return -1


if __name__ == "__main__":
    text = "JIM SAW ME IN A BARBERSHOP"
    pattern = "BARBER"
    for function in (bruteForce, horspool, horspool2):
        resetCounters()
        print(function.__name__, function(text, pattern), getCounters())
