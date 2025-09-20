# To convert a list to a dictionary with elemnts as keys and their counts as values

ls = [1, 2, 3, 2, 5, 1]
d = {}

def dict_convert(ls):
    for i in ls:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    return d

def remove_duplicates(ls):
    unique_ls = []
    for j in ls:
        if j not in unique_ls:
            unique_ls.append(j)
    return unique_ls

print()
print(f"Dictionary = {dict_convert(ls)}")
print(f"Unique List = {remove_duplicates(ls)}")
print()