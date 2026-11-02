"""Combine both Boyer-Moore shifts. Run: python -m java6.detyra5.main

The supplied Task 5 repeats Task 4. This implements boyerMoore, required
by Task 1's export list, using the good-suffix table from Task 4.
"""

from java6.detyra1 import main as search_state
from java6.detyra4.main import goodSuffixTable


def boyerMoore(T, P):
    """Return the first match position, or -1 when no occurrence exists."""
    n, m = len(T), len(P)
    if m == 0:
        return 0

    bad_character = search_state.shiftTable(P)
    good_suffix = goodSuffixTable(P)
    i = m - 1
    while i < n:
        search_state.record_alignment()
        k = 0
        while k < m and search_state.compare_characters(P[m - 1 - k], T[i - k]):
            k += 1
        if k == m:
            return i - m + 1

        # The mismatch is k places left of the window end. Subtract k from
        # the table distance to align an earlier occurrence with that spot.
        # Clamp to 1 so every iteration makes forward progress.
        bad_shift = max(1, bad_character.get(T[i - k], m) - k)
        # Both rules are safe independently; take the larger shift.
        # When k = 0, no suffix matched, so good_suffix[0] contributes 0.
        i += max(bad_shift, good_suffix[k])
    return -1


if __name__ == "__main__":
    search_state.resetCounters()
    print(boyerMoore("JIM SAW ME IN A BARBERSHOP", "BARBER"))
    print(search_state.getCounters())
