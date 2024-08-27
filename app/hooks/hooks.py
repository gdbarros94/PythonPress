hooks = {
    'actions': {},
    'filters': {}
}

def add_action(hook_name, func):
    if hook_name not in hooks['actions']:
        hooks['actions'][hook_name] = []
    hooks['actions'][hook_name].append(func)

def do_action(hook_name, *args, **kwargs):
    if hook_name in hooks['actions']:
        for func in hooks['actions'][hook_name]:
            func(*args, **kwargs)

def add_filter(hook_name, func):
    if hook_name not in hooks['filters']:
        hooks['filters'][hook_name] = []
    hooks['filters'][hook_name].append(func)

def apply_filters(hook_name, value, *args, **kwargs):
    if hook_name in hooks['filters']:
        for func in hooks['filters'][hook_name]:
            value = func(value, *args, **kwargs)
    return value
