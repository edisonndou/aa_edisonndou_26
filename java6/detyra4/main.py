"""Build strong good-suffix shifts. Run: python -m java6.detyra4.main"""


def goodSuffixTable(P):
    """Return d2[k], the safe shift after matching k trailing characters."""
    m = len(P)
    d2 = [0] * m
    # Preprocessing compares pattern characters with other pattern characters,
    # so these comparisons must not contribute to the search counters.
    for k in range(1, m):
        suffix_start = m - k
        found = False
        # Scan right to left to find the closest acceptable copy. Copies
        # may overlap the suffix at the end of the pattern.
        for start in range(suffix_start - 1, -1, -1):
            j = 0
            while j < k and P[start + j] == P[suffix_start + j]:
                j += 1
            if j == k and (start == 0 or P[start - 1] != P[suffix_start - 1]):
                d2[k] = suffix_start - start
                found = True
                break
        if found:
            continue

        # No suitable copy: keep the longest prefix equal to a suffix of
        # the matched characters. With no such prefix, shift the full m.
        d2[k] = m
        for length in range(k - 1, 0, -1):
            j = 0
            while j < length and P[j] == P[m - length + j]:
                j += 1
            if j == length:
                d2[k] = m - length
                break
    # Empty patterns yield []; otherwise d2[0] stays 0 (no matched suffix).
    return d2


if __name__ == "__main__":
    for pattern in ("ABCBAB", "BAOBAB", "tatëpjetë"):
        print(pattern, goodSuffixTable(pattern))
