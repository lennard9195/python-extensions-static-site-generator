_callbacks = {}


def register(hook: str, order: int = 0):
    def register_callback(func):
        _callbacks.setdefault(hook, {}).setdefault(order, []).append(func)
        return func
    return register_callback


def event(hook: str, *args):
    for order in sorted(_callbacks.get(hook, {})):
        for func in _callbacks[hook][order]:
            func(*args)


def filter(hook: str, value, *args):
    for order in sorted(_callbacks.get(hook, {})):
        for func in _callbacks[hook][order]:
            value = func(value, *args)
    return value
