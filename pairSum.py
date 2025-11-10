inp = [7, 3, 5, 2]
s = 3

def pair_sum(arr, target):
    seen = set()
    result = []
    for num in arr:
        complement = target - num
        if complement in seen:
            result.append(f"{complement} + {num} = {target}")
        seen.add(num)
    return bool(result), result

found, pairs = pair_sum(inp, s)
print(f"Found pairs: {found}") 
if found:
    for p in pairs:
        print(p)
else:
    print("No pairs found")