# coding=utf-8


if __name__ == '__main__':
    # Python内置非常强大，可以用来创建list的生成式
    print range(1, 11)
    L = []
    for x in range(1, 11):
        L.append(x ** x)
    print L
    print [x * x for x in range(1, 11) if x % 2 == 0]
    print [m + n for m in 'ABC' for n in 'XYZ']

    d = {'x': 'A', 'y': 'B', 'z': 'C'}
    print [k + '=' + v for k, v in d.iteritems()]
    L = ['Hello', 'World', 'IBM', 'Apple', None]
    print [s.lower() for s in L if isinstance(s, str)]
