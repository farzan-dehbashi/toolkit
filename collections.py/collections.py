import collections

a = 'aaaabbbcc'
my_counter = collections.Counter(a)

# the number each char is repeated
print(my_counter)

print(my_counter.most_common(1))