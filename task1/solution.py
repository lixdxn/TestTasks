from functools import wraps
import inspect

def strict(func):
    annotations = func.__annotations__

    @wraps(func)
    def wrapper(*args, **kwargs):
        bound = inspect.signature(func).bind(*args, **kwargs)
        for name, value in bound.arguments.items():
            if name in annotations and not isinstance(value, annotations[name]):
                raise TypeError(f"Argument '{name}' must be {annotations[name].__name__}, got {type(value).__name__}")
        return func(*args, **kwargs)
    return wrapper

@strict
def sum_two(a: int, b: int) -> int:
    return a + b
