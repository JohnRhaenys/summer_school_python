def get_function_runtime(function, args=None):
    """
    Return the number of seconds it takes to run a function
    :param function: the function that will be run
    :param args: the arguments of the function, if there are any
    :return: the time, in seconds
    """
    import time
    start_time = time.time()
    function(args)
    end_time = time.time()
    return (end_time - start_time) * 1000
