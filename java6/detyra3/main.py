# TASK 2 — WRITE
# highlight(T, P)
# STEPS
# 1. Get the matches with findAll.
# 2. Walk through the text and build a new string, character by character.
# 3. Put [ before and ] after every match.
# 4. Skip a match that starts inside the previous highlighted one.
# REQUIREMENTS
# - Returns a new string.
# - No built-in replace or split.
# - No match: the text comes back unchanged.
# CHECK
# highlight(kur, 'pjetë')
# // → 'Kur ngjite për[pjetë], shiko dhe tatë[pjetë].'

# highlight('banana', 'ana')
# // → 'b[ana]na'