# Task 1 - Trace

```python
T = "JIM SAW ME IN A BARBERSHOP"
P = "BARBER"
```

The `bruteForce`, `shiftTable`, `shift`, `horspool`, and `horspool2` implementations are
translated from the supplied lecture code into Python. A Python dictionary
replaces the JavaScript `Map`. The `shift` helper returns a stored shift when
the character is present, or the pattern length otherwise. The alignment logging
from the original task is retained. An empty pattern returns 0 explicitly.

The supplied `horspool2` shifts using `T[i - k]` instead of `T[i]`. This rule
skips the match even in this lecture example: its result is `-1`, contrary to
the supplied prediction of `16`. The code preserves the lecture's rule so this
difference can be studied.

## Predictions (worked out before execution)

The Python translation has not been executed because neither `python` nor `py`
is available in this shell. The Real column below is reserved for Python execution.

| Function | Predicted | Real |
| --- | --- | --- |
| `shiftTable(P)` | `{'B': 2, 'A': 4, 'R': 3, 'E': 1}`; other characters shift by 6 | Pending Python execution |
| `bruteForce(T, P)` | `16` | Pending Python execution |
| `horspool(T, P)` | `16` | Pending Python execution |
| `horspool2(T, P)` | Supplied prediction: `16`; corrected by manual trace: `-1` | Pending Python execution |

Python indexes start at zero. `BARBER` occupies indexes 16 through 21.

## Shift table

For pattern length `m = 6`, process pattern indexes `0` through `m - 2`.
Set each character's shift to `m - 1 - j`. Later occurrences overwrite earlier
ones. The first `B` initially gets shift 5, then the second `B` overwrites it
with 2. Exclude the final `R`, so it does not produce a zero shift.

| Character | Rightmost index before the final character | Shift |
| --- | --- | --- |
| `B` | 3 | 2 |
| `A` | 1 | 4 |
| `R` | 2 | 3 |
| `E` | 4 | 1 |
| Any other character | Absent | 6 |

## Horspool alignment trace

Compare each alignment from right to left. After a mismatch, choose the shift
using the text character under the **last pattern position**.

| Alignment start | End index `i` | Text window | End character | Outcome |
| --- | --- | --- | --- | --- |
| 0 | 5 | `JIM SA` | `A` | Mismatch; shift 4 |
| 4 | 9 | `SAW ME` | `E` | Mismatch; shift 1 |
| 5 | 10 | `AW ME ` | Space | Mismatch; shift 6 |
| 11 | 16 | `IN A B` | `B` | Mismatch; shift 2 |
| 13 | 18 | ` A BAR` | `R` | Last `R` matches, then `E` mismatches `A`; shift 3 |
| 16 | 21 | `BARBER` | `R` | All six characters match; return 16 |

The match ends at index 21, so its starting index is `21 - 6 + 1 = 16`.

The first line inside the outer `while` loop of `horspool` is
`print(i - m + 1)`, the Python equivalent of the requested logging. It prints
`0, 4, 5, 11, 13, 16`, each on
its own line.

## Horspool2 trace (corrected)

| Step | Alignment start | End index `i` | Matched characters `k` | Mismatch `T[i - k]` | Shift | Next `i` |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | 0 | 5 | 0 | `A` | 4 | 9 |
| 2 | 4 | 9 | 0 | `E` | 1 | 10 |
| 3 | 5 | 10 | 0 | Space | 6 | 16 |
| 4 | 11 | 16 | 0 | `B` | 2 | 18 |
| 5 | 13 | 18 | 1 | `A` at index 17 | 4 | 22 |
| 6 | 17 | 22 | 0 | `S` | 6 | 28 |

At `i = 18`, `P[5]` and `T[18]` are both `R`, so `k` becomes 1.
Then `P[4] = 'E'` mismatches `T[17] = 'A'`. Standard `horspool` shifts by
`shift(table, T[18], 6) = 3`, reaching the matching end index 21.
However, `horspool2` shifts by `shift(table, T[17], 6) = 4`, reaching 22 and
skipping that match. After shifting to 28, the loop ends because `len(T) = 26`.
It returns `-1`. Its alignment starts are `0, 4, 5, 11, 13, 17`.

## Run

From the repository root:

```powershell
python java4/detyra/detyra1/search.py
```

The console prints the Horspool alignments, then a table with Function,
Predicted, and Real columns. Descriptions for all four functions appear after
the table, including why `horspool2` returns `-1` despite the match:

```text
Descriptions:
shiftTable: Repeated B overwrites 5 with 2; other characters shift 6.
bruteForce: BARBER starts at index 16 (counting from zero).
horspool: Safe shifts reach index 16 and find BARBER.
horspool2: -1 means no match found; the mismatch shift skips BARBER.
At i=18, R matches, so k=1. Then E mismatches A at index 17.
Shifting by 4 moves i to 22, skipping the match ending at 21.
The next shift moves i to 28, outside the text, so it returns -1.
```

Column widths are calculated from the contents. The Real column is populated
by function calls when the script runs; Predicted preserves the supplied predictions.
