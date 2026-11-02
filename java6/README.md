# Java 6 - string-search exercises in Python

Here `java6` means week 6; these solutions use Python, as requested.
Each folder contains its implementation and explanatory comments. The shared
`search.py` exposes the complete API without duplicating the algorithms.

| Folder | Implementation |
| --- | --- |
| `detyra1` | Counters, `bruteForce`, `shiftTable`, `horspool`, `horspool2` |
| `detyra2` | `findAll`, including overlapping matches |
| `detyra3` | `highlight`, skipping overlapping highlights |
| `detyra4` | `goodSuffixTable`, including the prefix fallback |
| `detyra5` | `boyerMoore`, combining bad-character and good-suffix shifts |

The supplied `detyra5` instructions duplicate `detyra4`. The fifth solution
implements `boyerMoore`, which the assignment's required export list names.
The JavaScript export requirement is translated into `java6/search.py` and
its Python `__all__` list.

## Run

With Python 3 installed, run from the repository root:

```powershell
python -m java6.detyra1.main
python -m java6.detyra2.main
python -m java6.detyra3.main
python -m java6.detyra4.main
python -m java6.detyra5.main
```

Use module commands so imports between exercise folders resolve correctly.
The files print examples only when run as the main module; imports are quiet.
No third-party packages are needed.

## Shared API

```python
from java6.search import (
    bruteForce, shiftTable, horspool, horspool2,
    findAll, highlight, goodSuffixTable, boyerMoore,
    resetCounters, getCounters,
)
```

- Positions are zero-based Python Unicode character indexes.
- First-match searches return `-1` if there is no match.
- `findAll` returns all positions in order, or `[]` if there are none.
- Empty patterns return `0` for first-match searches and every text boundary
  for `findAll`. `highlight` leaves text unchanged for an empty pattern.
- Counters accumulate until `resetCounters()` is called. A comparison counts
  every pattern-to-text character comparison, including failures. An alignment
  counts every actual nonempty-pattern placement. Empty-pattern operations and
  table preprocessing add no counts.
- `highlight` gets its search counts from `findAll`; copying the output does
  not add search comparisons or alignments.
- No built-in substring searches, replacement, splitting, or regex are used.

`horspool2` intentionally preserves the earlier lecture variant, whose
unadjusted mismatch-character shift can skip valid occurrences. Use `horspool`
or `boyerMoore` for a correct first-match search.

## Assignment examples (expected, not executed)

For `kur = 'Kur ngjite përpjetë, shiko dhe tatëpjetë.'`:

- `findAll(kur, 'pjetë')` gives `[14, 35]`. After resetting counters first,
  this search uses 20 comparisons and 10 alignments.
- `findAll('banana', 'ana')` gives `[1, 3]`.
- `highlight(kur, 'pjetë')` gives
  `'Kur ngjite për[pjetë], shiko dhe tatë[pjetë].'`.
- `highlight('banana', 'ana')` gives `'b[ana]na'`.
- `goodSuffixTable('ABCBAB')` gives `[0, 2, 4, 4, 4, 4]`.
- `goodSuffixTable('BAOBAB')` gives `[0, 2, 5, 5, 5, 5]`.
- `goodSuffixTable('tatëpjetë')` gives `[0, 9, 5, 9, 9, 9, 9, 9, 9]`.

Tests were not written or run, per the project's testing preference. Python
was unavailable in the implementation shell, so interpreter syntax checking
was not performed either.
