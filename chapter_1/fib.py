#!/usr/bin/env python
# -*- coding:utf-8 -*-
import time

def log_cost_time(func):
    def wrapped(*args, **kwargs):
        import time
        begin = time.time()
        try:
            return func(*args, **kwargs)
        finally:
            print('func %s cost %s s' % (func.__name__, time.time() - begin))
    return wrapped


class Solution(object):
    @log_cost_time
    def fib_with_recursion(self, n):
        def _fib(n):
            if n < 2:
                return 1
            else:
                return _fib(n - 1) + _fib(n -2 )
        ret = _fib(n)
        return ret

    @log_cost_time
    def fib_with_recurrence(self, n):
        f1 = f2 = 1
        for _ in range(1, n):
            f1, f2 = f2, f2 + f1
        return f2



if __name__ == '__main__':
    s = Solution()
    print(s.fib_with_recursion(35))
    print(s.fib_with_recurrence(35))    

