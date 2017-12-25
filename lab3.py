def rm_adj(nums):
    return list(set(nums))

def two(list1, list2):
    new = []
    new.extend(list1)
    new.extend(list2)
    new.sort()
    return new

a = [0, 2, 2, 3]
b = list(set(a))
print(b)

a = [1, 2, 5, 7, 9, 11]
b = [2,4,10,12]
c = two(a,b)
print(c)