def flag(union, name):
    return hasattr(union, name) and getattr(union, name)
