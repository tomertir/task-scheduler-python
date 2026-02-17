def id_generator(n):
    if n <= 0:
        raise ValueError("n must be a int greater than zero")
    for i in range(n):
        yield i
        
