# TASK 2 — WRITE
# goodSuffixTable(P)
# STEPS
# For each k = 1 ... m - 1 (the suffix is the last k characters):
# 1. Look to the left for the rightmost other copy of the suffix that is not preceded by the same character as the suffix. A copy at the very start of the pattern counts.
# 2. Found: d2[k] = the distance between that copy and the suffix.
# 3. Not found: take the longest prefix of size l < k that equals the suffix of size l; d2[k] = m - l (m if there is none).
# REQUIREMENTS
# - Returns an array of length m, with d2[0] = 0.
# - Works for any characters.
# CHECK
# goodSuffixTable('ABCBAB')
# // → [0, 2, 4, 4, 4, 4]

# goodSuffixTable('BAOBAB')
# // → [0, 2, 5, 5, 5, 5]

# goodSuffixTable('tatëpjetë')
# // → [0, 9, 5, 9, 9, 9, 9, 9, 9]