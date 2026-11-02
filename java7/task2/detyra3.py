# task2/detyra3.py
# Maximum comparisons for three hashing methods

from detyra1 import h, num, chainedTable, probeInsert
from detyra2 import doubleHashInsert


# -----------------------------------------
# MAXIMUM COMPARISONS
# -----------------------------------------

def maxComparisons(keys, m):
    """
    Calculate the maximum number of key comparisons
    in a successful search using:

    1. Separate chaining
    2. Linear probing
    3. Double hashing

    Returns:
        {
            "chained": number,
            "linear": number,
            "double": number
        }

    Requirements:
    - Keys must be distinct.
    - Number of keys must be smaller than m.
    - Original keys must not be modified.
    """

    if m <= 2:
        raise ValueError("Table size must be greater than 2")

    if len(keys) >= m:
        raise ValueError("Number of keys must be less than m")

    if len(set(keys)) != len(keys):
        raise ValueError("Keys must be distinct")

    # -------------------------------------
    # 1. BUILD THREE HASH TABLES
    # -------------------------------------

    # Separate chaining
    chained = chainedTable(keys, m)

    # Linear probing
    linear = [None] * m

    for key in keys:
        probeInsert(linear, key)

    # Double hashing
    double = [None] * m

    for key in keys:
        doubleHashInsert(double, key)

    # -------------------------------------
    # 2. CHAINED HASHING
    # -------------------------------------

    # Longest chain represents maximum
    # successful-search comparisons.

    max_chained = max(
        (len(chain) for chain in chained),
        default=0
    )

    # -------------------------------------
    # 3. LINEAR PROBING
    # -------------------------------------

    max_linear = 0

    for key in keys:

        i = h(key, m)
        comparisons = 0

        for _ in range(m):

            comparisons += 1

            if linear[i] == key:
                break

            i = (i + 1) % m

        max_linear = max(
            max_linear,
            comparisons
        )

    # -------------------------------------
    # 4. DOUBLE HASHING
    # -------------------------------------

    max_double = 0

    for key in keys:

        i = h(key, m)

        # Second hash function
        s = m - 2 - num(key) % (m - 2)

        comparisons = 0

        for _ in range(m):

            comparisons += 1

            if double[i] == key:
                break

            i = (i + s) % m

        max_double = max(
            max_double,
            comparisons
        )

    # -------------------------------------
    # 5. RETURN RESULTS
    # -------------------------------------

    return {
        "chained": max_chained,
        "linear": max_linear,
        "double": max_double
    }


# -----------------------------------------
# MAIN PROGRAM
# -----------------------------------------

if __name__ == "__main__":

    # Professor's numeric example
    N = [30, 20, 56, 75, 31, 19]

    # Professor's word example
    W = [
        "A", "FOOL", "AND", "HIS",
        "MONEY", "ARE", "SOON", "PARTED"
    ]

    print("=" * 60)
    print("TASK 2 - EXERCISE 3: MAX COMPARISONS")
    print("=" * 60)

    # -------------------------------------
    # TEST 1: NUMERIC KEYS
    # -------------------------------------

    result1 = maxComparisons(N, 11)

    print("\nTEST 1: maxComparisons(N, 11)")
    print("Keys:", N)
    print("Result:", result1)

    # -------------------------------------
    # TEST 2: STRING KEYS
    # -------------------------------------

    result2 = maxComparisons(W, 13)

    print("\nTEST 2: maxComparisons(W, 13)")
    print("Keys:", W)
    print("Result:", result2)

    # -------------------------------------
    # VERIFY PROFESSOR'S EXPECTED RESULTS
    # -------------------------------------

    expected1 = {
        "chained": 3,
        "linear": 6,
        "double": 2
    }

    expected2 = {
        "chained": 2,
        "linear": 2,
        "double": 3
    }

    assert result1 == expected1, (
        f"Test 1 failed: {result1}"
    )

    assert result2 == expected2, (
        f"Test 2 failed: {result2}"
    )

    print("\nSUCCESS: ALL TESTS PASSED!")
