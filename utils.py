def get_function_runtime(function, args=None):
    """
    Return the number of seconds it takes to run a function
    :param function: the function that will be run
    :param args: the arguments of the function, if there are any
    :return: the time, in seconds
    """
    import time
    if args:
        start_time = time.time()
        function(args)
    else:
        start_time = time.time()
        function()
    return (time.time() - start_time) * 1000
