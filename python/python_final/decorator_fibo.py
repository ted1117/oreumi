import time
import functools

def clock(func):
    @functools.wraps(func)
    def clocked(*args, **kwargs):
        t0 = time.time()
        result = func(*args, **kwargs)  # 함수 실행
        elasped = time.time() - t0      # 함수가 실행된 시간
        name = func.__name__
        arg_list = []
        if args:
            arg_list.append(", ".join(repr(arg) for arg in args))
        if kwargs:
            pairs = ["%s=%r" % (k, w) for k, w in sorted(kwargs.items())]
            arg_list.append(", ".join(pairs))
        arg_str = ", ".join(arg_list)
        print('[%0.8fs] %s(%s) -> %r' % (elasped, name, arg_str, result))
        return result
    return clocked

@functools.cache
@clock
def fibonacci(n):
    # return fibonacci(n-1) + fibonacci(n-2) if n >= 2 else n
    return n if n < 2 else fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(6))