# coding=utf-8
from collections import Iterable

if __name__ == '__main__':
    print isinstance('abc', Iterable)

    d = {'a': 1, 'b': 2, 'c': 3}
    for key in d:
        print key
    for value in d.itervalues():
        print value
    for value in d.iteritems():
        print value
    print isinstance(d, Iterable)
    print d.keys(), d.items(), d.values()
    print d.iterkeys()

    # 在遍历的过程中，同时迭代索引和元素本身
    for i, value in enumerate(['a', 'b', 'c']):
        print i, value
    for x, y in [(1, 'a'), (2, 'b'), (3, 'c')]:
        print x, y

    L = ['Hello', 'world', 2016, 1114]
    newL = [isinstance(s, str) and s.lower() or s for s in L]
    print newL
