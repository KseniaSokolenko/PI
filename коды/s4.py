class Trace:
    def __init__(self):
        self.enabled = True

    def __call__(self, f):
        def wrap(*args, **kwargs):
            if self.enabled:
                print(f'Calling {f}')
            return f(*args, **kwargs)
        return wrap
tracer = Trace()

@tracer
def rotate_list(l):
    return l[1:] + [l[0]]

l = [1, 2, 3]
l = rotate_list(l)
print(l)

def square_list(l):
    return [x**2 for x in l]
l = [1, 2, 3]
l = square_list(l)
print(l)

