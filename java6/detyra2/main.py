# TASK 2 — WRITE
# findAll(T, P)
# STEPS
# 1. Start from horspool.
# 2. alignments++ each time round the outer loop; comparisons++ before every character comparison.
# 3. On a full match, save i - m + 1 and keep going.
# 4. After a match, shift exactly as after a mismatch: by the table value of T[i].
# REQUIREMENTS
# - Returns the start of every match, in order.
# - Overlapping matches count.
# - [ ] if there is no match.
# CHECK
# const kur = 'Kur ngjite përpjetë, shiko dhe tatëpjetë.';

# findAll(kur, 'pjetë')     // → [14, 35]

# findAll('banana', 'ana')  // → [1, 3]


# Counters: 20 comparisons, 10 alignments.