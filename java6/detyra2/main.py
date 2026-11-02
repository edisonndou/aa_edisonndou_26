"""Find all matches, including overlaps. Run: python -m java6.detyra2.main"""

from java6.detyra1 import main as search_state


def findAll(T, P):
    """Continue Horspool after every match instead of returning immediately."""
    n, m = len(T), len(P)
    # An empty pattern occurs at every boundary, including after the text.
    # No character comparisons or search alignments are needed in this case.
    if m == 0:
        return list(range(n + 1))

    table = search_state.shiftTable(P)
    positions = []
    i = m - 1
    while i < n:
        search_state.record_alignment()
        k = 0
        while k < m and search_state.compare_characters(P[m - 1 - k], T[i - k]):
            k += 1
        if k == m:
            positions.append(i - m + 1)
        # The same shift applies after a match and a mismatch. Moving by m
        # after a match would lose overlaps, such as the two ana in banana.
        i += table.get(T[i], m)
    return positions


if __name__ == "__main__":
    text = "Kur ngjite përpjetë, shiko dhe tatëpjetë."
    search_state.resetCounters()
    print(findAll(text, "pjetë"))
    print(search_state.getCounters())
    search_state.resetCounters()
    print(findAll("banana", "ana"))
    print(search_state.getCounters())
