# Write a code to find the consecutive differences from a list and give the maximum number as output (No negative)

def consecutive_differences(lst):
    if len(lst) < 2:
        return [], 0

    diffs = []
    for i in range(1, len(lst)):
        diffs.append(abs(lst[i] - lst[i - 1]))

    return diffs, max(diffs)

lst = [1, 5, 3, 9, 2]
diffs, max_diff = consecutive_differences(lst)

print()

print(f"Input list: {lst}")
print(f"Consecutive differences: {diffs}")
print("The maximum consecutive difference is:", max_diff)

print()