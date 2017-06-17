def does_something(arg):
    """
    take one arg and does something bases on type
	if arg is a string ,return arg * 3 
	if arg is an int or float ,return arg + 10 
    """
    if isinstance(arg, (int, float)):
        return arg + 10
    elif isinstance(arg, str):
        return str * 3
    else:
        raise TypeError("does_something only takes ints, floats, and strings")
