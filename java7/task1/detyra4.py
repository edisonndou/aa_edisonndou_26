
# detyra4.py
# TASK 4: Complete Hashing Trace
# Predicted vs. Real Results

from detyra1 import chainedTable
from detyra2 import probeInsert, probeFind
from detyra3 import probeRemove


# Step 1: Input data
W = [
    "A", "FOOL", "AND", "HIS",
    "MONEY", "ARE", "SOON", "PARTED"
]


# Step 2: Initialize hash table
T = [None] * 13


# Step 3: Insert all keys
for word in W:
    probeInsert(T, word)


print("=" * 85)
print("TASK 4: COMPLETE HASHING TRACE")
print("=" * 85)


# Display initial hash table
print("\nINITIAL HASH TABLE")

for i, value in enumerate(T):
    print(f"Index {i:2}: {value}")


# Step 4: Predicted results
predicted = [
    ["ARE", "SOON"],
    0,
    -1,
    11,
    -1
]


# Step 5: Function calls
calls = [
    "chainedTable(W, 13)[11]",
    "probeFind(T, 'PARTED')",
    "probeFind(T, 'KID')",
    "probeRemove(T, 'ARE')",
    "probeFind(T, 'SOON')"
]


# Step 6: Execute functions in order
real = [
    chainedTable(W, 13)[11],
    probeFind(T, "PARTED"),
    probeFind(T, "KID"),
    probeRemove(T, "ARE"),
    probeFind(T, "SOON")
]


# Step 7: Compare predicted and real results
print("\nPREDICTED VS REAL RESULTS")
print("-" * 95)

print(
    f"{'Function Call':<33}"
    f"{'Predicted':<22}"
    f"{'Real':<22}"
    f"{'Status'}"
)

print("-" * 95)

for call, prediction, result in zip(
    calls, predicted, real
):
    status = (
        "PASS" if prediction == result
        else "FAIL"
    )

    print(
        f"{call:<33}"
        f"{str(prediction):<22}"
        f"{str(result):<22}"
        f"{status}"
    )


# Step 8: Display final hash table
print("\nFINAL HASH TABLE AFTER REMOVAL")

for i, value in enumerate(T):
    print(f"Index {i:2}: {value}")


# Step 9: Verify predictions
assert predicted == real, "Results do not match!"

print("\nSUCCESS: All five predictions match.")
