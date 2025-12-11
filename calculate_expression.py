def f(expression):
    return sum(int(x) if x[0] != '-' else -int(x[1:]) for x in expression.replace('-', '+-').split('+'))
