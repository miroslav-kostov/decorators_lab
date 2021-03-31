def tags(tag_type):
    def decorator(func):
        def wrapper(*args):
            return f"<{tag_type}>{func(*args)}</{tag_type}>"
        return wrapper
    return decorator

@tags('p')
def join_strings(*args):
    return "".join(args)
print(join_strings("Hello", " you!"))
