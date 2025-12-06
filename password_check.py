def f(password):
    return len(password) >= 6 and len(set(password)) == len(password)
