#### 容器（Container）
容器是一种把多种元素组织在一起的数据结构，容器的元素可以逐个迭代获取，可以用 in，not in
来判断元素是否包含在容器中。

在 Python 中，常见的容器对象有：
* list,deque,...
* set,frozensets,...
* dict,defaultdict,OrderedDict,Counter,...
* tuple,namedtuple,...
* str

容器可以理解为一个放东西的物品。如果一个对象可以被用来询问某个元素是否包含在其中时，那么这
个对象就被认为是一个容器。

尽管绝大多数容器都提供了某种方式来获取其中的元素，但这并不是容器本身提供的能力，而是**可迭
代对象**赋予了容器这种能力。

#### 可迭代对象（iterable）
但凡是可以返回一个**迭代器**的对象都可以成为可迭代对象。
除了大部分容器是可迭代对象外，还有更多的对象也可以是可迭代对象，如打开状态的 files，
sockets 等。
```
>>> x = [1,2,3]
>>> y = iter(x)
>>> z = iter(y)
```
这里 x 是一个可迭代对象；
y 和 z 是两个独立的迭代器，迭代器内部持有一个状态，该状态用于记录当前迭代所在的位置，以便
下次迭代的时候获取正确的元素。

#### 迭代器（iterator）
迭代器是一个带状态的对象，他能在你调用 next() 方法的时候返回容器的下一个值，任何实现了
<span>__iter__</span> 和<span>__next__()</span>方法的对象都是迭代器，前者返回
迭代器本身，后者则返回容器的下一个值。


参考至 https://foofish.net/iterators-vs-generators.html
