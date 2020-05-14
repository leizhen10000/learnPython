#!/usr/bin/env python
# -*- coding: utf-8 -*-


from collections import deque


class LineHistory:
    """历史记录"""
    def __init__(self, lines, history_len=3):
        self.lines = lines
        self.history = deque(maxlen=history_len)

    def __iter__(self):
        for line_no, line in enumerate(self.lines, 1):
            self.history.append((line_no, line))
            yield line

    def clear(self):
        self.history.clear()


if __name__ == '__main__':
    with open('test.txt') as f:
        lines = LineHistory(f)
        for line in lines:
            if 'python' in line:
                for line_no, hline in lines.history:
                    print(f'{line_no}:{hline}', end='')
