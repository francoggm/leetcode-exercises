numbers = [4, -2, -1, 3]
numbers.sort()
n = len(numbers)
min_d = float('inf')
min_dict = {}

for i in range(n - 1):
    dif = abs(numbers[i+1] - numbers[i])
    min_dict.setdefault(dif, [])
    min_dict[dif].append([numbers[i], numbers[i+1]])
    min_d = min(min_d, dif)

for dif_list in min_dict[min_d]:
    print(dif_list[0], dif_list[1])




names = ['steve', 'stevens', 'danny', 'steves', 'dan', 'john', 'johnny', 'joe', 'alex', 'alexander']
query = ['steve', 'alex', 'joe', 'john', 'dan']

names_len = len(names)
queries_len = len(query)
output = []

for i in range(queries_len):
    count = 0
    prefix_len = len(query[i])
    for j in range(names_len):
        if not names[j] == query[i] and len(names[j]) > prefix_len:
            if query[i] == names[j][:prefix_len]:
                count += 1
    output.append(count)


import collections
binary = collections.deque()
binary.append(1)

binary

binary_decimal = binary.data
while binary.next is not None:
    binary_decimal = binary_decimal * 2 +  binary.next.val
    head = binary.next

hammer_count = 0
small_hammer = 0
big_hammer = 0

bigHits = 4
newtons = [3,2,5,4,6,7,9]
newtons.sort()

if len(newtons) <= bigHits:
    return [len(newtons), newtons, -1]
elif:
    if bigHits > 0:
        idx = bigHits - 1
        bigHits = newtons[idx+1:]
    else:
        idx = len(newtons) + 1
        bigHits = [-1]
    small_list = newtons[:idx]
    return [sum(small_list) + bigHits, bigHits]



