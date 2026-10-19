T = "JIM SAW ME IN A BARBERSHOP"
P = "BARBER"


def shiftTable(P):
    """Build shifts; characters absent from the table use len(P)."""
    m = len(P)
    table = {}

    for j in range(m - 1):
        table[P[j]] = m - 1 - j

    return table


def shift(table, c, m):
    """Return the stored shift, or the pattern length for other characters."""
    return table[c] if c in table else m


def bruteForce(T, P):
    """Python translation of the supplied lecture implementation."""
    n, m = len(T), len(P)

    for i in range(n - m + 1):
        j = 0

        while j < m and P[j] == T[i + j]:
            j += 1

        if j == m:
            return i

    # Every possible starting position was checked without finding a match.
    return -1


def horspool(T, P):
    """Translate the lecture algorithm, with the requested alignment logging."""
    n, m = len(T), len(P)
    if m == 0:
        return 0

    table = shiftTable(P)
    i = m - 1

    while i <= n - 1:
        print(i - m + 1)
        k = 0

        while k <= m - 1 and P[m - 1 - k] == T[i - k]:
            k += 1

        if k == m:
            return i - m + 1

        i += shift(table, T[i], m)

    return -1


def horspool2(T, P):
    """Lecture variant: shifting on the mismatch can skip valid matches."""
    n, m = len(T), len(P)
    if m == 0:
        return 0

    table = shiftTable(P)
    i = m - 1

    while i <= n - 1:
        k = 0

        while k <= m - 1 and P[m - 1 - k] == T[i - k]:
            k += 1

        if k == m:
            return i - m + 1

        # Unlike horspool, this uses the mismatch character, not the window end.
        # Here, i=18 and k=1 select T[17]='A': shift 4 skips the match ending at 21.
        i += shift(table, T[i - k], m)

    # -1 means this search found no match; its unsafe shifts can miss one.
    return -1


def print_results(rows):
    """Print the assignment results as an aligned console table."""
    headers = ("Function", "Predicted", "Real")
    cells = [headers] + [tuple(str(value) for value in row) for row in rows]
    widths = [max(len(row[column]) for row in cells) for column in range(len(headers))]
    separator = "+-" + "-+-".join("-" * width for width in widths) + "-+"

    print(separator)
    for index, row in enumerate(cells):
        print("| " + " | ".join(
            value.ljust(width) for value, width in zip(row, widths)
        ) + " |")
        if index == 0:
            print(separator)
    print(separator)


if __name__ == "__main__":
    print("horspool alignments:")
    horspool_result = horspool(T, P)
    print()
    print_results([
        ("shiftTable(P)", {"B": 2, "A": 4, "R": 3, "E": 1}, shiftTable(P)),
        ("bruteForce(T, P)", 16, bruteForce(T, P)),
        ("horspool(T, P)", 16, horspool_result),
        ("horspool2(T, P)", 16, horspool2(T, P)),
    ])
    print("\nDescriptions:")
    print("shiftTable: Repeated B overwrites 5 with 2; other characters shift 6.")
    print("bruteForce: BARBER starts at index 16 (counting from zero).")
    print("horspool: Safe shifts reach index 16 and find BARBER.")
    print("horspool2: -1 means no match found; the mismatch shift skips BARBER.")
    print("At i=18, R matches, so k=1. Then E mismatches A at index 17.")
    print("Shifting by 4 moves i to 22, skipping the match ending at 21.")
    print("The next shift moves i to 28, outside the text, so it returns -1.")
