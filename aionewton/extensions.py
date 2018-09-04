from . import wrapper

# Expose basic endpoints
wrapper.expose_endpoints(wrapper.sys.modules[__name__], *wrapper.ENDPOINTS)


# Extensions for complex functions.
def log(exp, base=None):
    return wrapper.log(f'{base:d}|{exp}' if base else exp)


def tangent(exp, x=None):
    return wrapper.tangent(f"{x:d}|{exp}" if x else exp)


def area(exp, start=None, end=None):
    return wrapper.area(f'{start:d}:{end:d}|{exp}' if start and end else exp)
