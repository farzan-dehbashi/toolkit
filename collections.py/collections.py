import collections

a = 'aaaabbbcc'
my_counter = collections.Counter(a)

# the number each char is repeated
print(my_counter)

print(my_counter.most_common(1))


################################### Named tuple
My_named_tuple_class = collections.namedtuple('My_named_tuple_class','arg1,arg2')
pt = My_named_tuple_class(1,-4)
print(pt.arg1,pt.arg2)