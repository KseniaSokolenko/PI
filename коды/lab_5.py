def useless(lst):
    return max(lst) / len(lst)

print(useless([3,5,7,33]))
print(useless([-3,5.3,7,-33.4]))
print(useless([-3.45,5.4,-7,0.33]))
